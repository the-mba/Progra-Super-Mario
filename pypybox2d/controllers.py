#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# C++ version Copyright (c) 2006-2011 Erin Catto http://www.box2d.org
# Python port by Ken Lauer / http://pybox2d.googlecode.com
# 
# This software is provided 'as-is', without any express or implied
# warranty.  In no event will the authors be held liable for any damages
# arising from the use of this software.
# Permission is granted to anyone to use this software for any purpose,
# including commercial applications, and to alter it and redistribute it
# freely, subject to the following restrictions:
# 1. The origin of this software must not be misrepresented; you must not
# claim that you wrote the original software. If you use this software
# in a product, an acknowledgment in the product documentation would be
# appreciated but is not required.
# 2. Altered source versions must be plainly marked as such, and must not be
# misrepresented as being the original software.
# 3. This notice may not be removed or altered from any source distribution.

import math
from .common import (Vec2, property)
from .settings import (EPSILON, )

class Controller(object):
    """
    Base class for controllers.
    Controllers are for conveniently encapsulating common per-step
    functionality.
    """
    def __init__(self, world, bodies=[]):
        self._bodies = []
        self._world = world

        for body in bodies:
            self.add_body(body)

    @property
    def bodies(self):
        """The bodies affected by this controller"""
        return list(self._bodies)

    @property
    def world(self):
        """The world this controller acts in"""
        return self._world

    def step(self, timestep):
        """Controllers override this to implement per-step functionality."""
        raise NotImplementedError

    def add_body(self, body):
        """Adds a body to the controller list"""
        bodies = self._bodies
        if body in bodies:
            raise ValueError('Body already in controller')
        elif not body:
            raise ValueError('Body unset')
        elif body._world != self._world:
            raise ValueError('Body not in same world')

        bodies.append(body)
        body._attached_to_controller(self)

    def remove_body(self, body):
        """Removes a body from the controller list"""
        bodies = self._bodies
        if not body:
            raise ValueError('Body unset')
        elif body not in bodies:
            raise ValueError('Body not in controller')

        bodies.remove(body)
        body._detached_from_controller(self)

    def clear(self):
        for body in list(self._bodies):
            self.remove_body(body)


class BuoyancyController(Controller):
    """Calculates buoyancy forces for fluids in the form of a half plane."""
    def __init__(self, world, bodies=[], 
                 normal=(0,1), offset=0, density=0, velocity=(0,0),
                 linear_drag=0, angular_drag=0, use_density=False,
                 gravity=None):
        """
        normal        The outer surface normal
        offset        The height of the fluid surface along the normal
        density       The fluid density
        velocity      Fluid velocity, for drag calculations
        linear_drag   Linear drag co-efficient
        angular_drag  Angular drag co-efficient
        use_density   If false, bodies are assumed to be uniformly dense, 
                      otherwise use the shapes densities
        gravity       Gravity vector, uses world gravity if set to None
        """
        Controller.__init__(self, world, bodies)

        self.normal = normal
        self.offset = offset
        self.density = density
        self.velocity = velocity
        self.linear_drag = linear_drag
        self.angular_drag = angular_drag
        self.use_density = use_density
        self.gravity = gravity

    @property
    def normal(self):
        """The outer surface normal"""
        return self._normal
    @normal.setter
    def normal(self, normal):
        self._normal = Vec2(*normal)
   
    @property
    def offset(self):
        """The height of the fluid surface along the normal"""
        return self._offset
    @offset.setter
    def offset(self, offset):
        self._offset = float(offset)
   
    @property
    def density(self):
        """The fluid density"""
        return self._density
    @density.setter
    def density(self, density):
        self._density = float(density)
   
    @property
    def velocity(self):
        """Fluid velocity, for drag calculations"""
        return self._velocity
    @velocity.setter
    def velocity(self, velocity):
        self._velocity = Vec2(*velocity)
   
    @property
    def linear_drag(self):
        """Linear drag co-efficient"""
        return self._linear_drag
    @linear_drag.setter
    def linear_drag(self, linear_drag):
        self._linear_drag = float(linear_drag)
   
    @property
    def angular_drag(self):
        """Angular drag co-efficient"""
        return self._angular_drag
    @angular_drag.setter
    def angular_drag(self, angular_drag):
        self._angular_drag = float(angular_drag)
    
    @property
    def use_density(self):
        """
        If false, bodies are assumed to be uniformly dense,
        otherwise use the shapes densities
        """
        return self._use_density
    @use_density.setter
    def use_density(self, use_density):
        self._use_density = bool(use_density)

    @property
    def gravity(self):
        """Gravity vector, uses world gravity if set to None"""
        return self._gravity
    @gravity.setter
    def gravity(self, gravity):
        if gravity is not None:
            self._gravity = Vec2(*gravity)
        else:
            self._gravity = None

    def step(self, timestep):
        """Controllers override this to implement per-step functionality."""
        if not self._gravity:
            gravity = self._world._gravity
        else:
            gravity = self._gravity
        
        # Buoyancy force is just a function of position, so
        # unlike most forces, it is safe to ignore sleeping bodies.
        bodies = [body for body in self._bodies if body.awake]

        normal, offset = self._normal, self._offset

        for body in bodies:
            area_c, mass_c = Vec2(0, 0), Vec2(0, 0)
            area, mass = 0.0, 0.0
            xf = body._xf
            for fixture in body.fixtures:
                shape = fixture.shape

                if self._use_density:
                    shape_density = shape.density
                else:
                    shape_density = 1.0

                s_area, sc = shape.compute_submerged_area(normal, offset, xf, shape_density)
                area += s_area
                area_c += s_area * sc

                mass += s_area * shape_density
                mass_c += (s_area * shape_density) * sc

            if area >= EPSILON:
                area_c /= area
                mass_c /= mass

                # Buoyancy
                buoyancy_force = -self._density * area * gravity
                body.apply_force(buoyancy_force, mass_c)

                # Linear drag
                lin_vel = body.get_linear_velocity_from_world_point(area_c)
                drag_force = (lin_vel - self._velocity) * (-self._linear_drag * area)
                body.apply_force(drag_force, area_c)

                # Angular drag
                # UPSTREAM_TODO: Something that makes more physical sense?
                body.apply_torque(-body.inertia / body.mass * area * 
                                  body._angular_velocity * self._angular_drag)



class GravityController(Controller):
    """Applies simplified gravity between every pair of bodies"""
    def __init__(self, world, bodies=[], 
                 G=1.0, inv_sqr=True):
        """
        G - the strength of the gravitation force
        inv_sqr - If True, gravity is proportional to 1/r^2, otherwise 1/r
        """
        Controller.__init__(self, world, bodies)

        self.G = G
        self.inv_sqr = inv_sqr

    @property
    def G(self):
        """The strength of the gravitation force"""
        return self._G
    @G.setter
    def G(self, G):
        self._G = float(G)
   
    @property
    def inv_sqr(self):
        """inv_sqr - If True, gravity is proportional to 1/r^2, otherwise 1/r"""
        return self._inv_sqr
    @inv_sqr.setter
    def inv_sqr(self, inv_sqr):
        self._inv_sqr = bool(inv_sqr)
   
    def step(self, timestep):
        def bodies():
            for body1 in self._bodies:
                for body2 in self._bodies:
                    if body1 != body2:
                        yield body1, body2
       
        masses = dict((body, body.mass) for body in self._bodies)
        G = self._G
        inv_sqr = self._inv_sqr

        for body1, body2 in bodies():
            d = body2.world_center - body1.world_center
            r2 = d.length_squared
            f = G / r2 * masses[body1] * masses[body2] * d
            if inv_sqr:
                f /= math.sqrt(r2)

            body1.apply_force(f, body1.world_center)
            body2.apply_force(-f, body2.world_center)
            
