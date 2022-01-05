import pyxel, math
import numpy as np

from Helper import *

class Entity:
    def __init__(self, game, BLOCK_TYPE: BLOCK_TYPES, STARTING_X: float, STARTING_Y: float, STARTING_VEL_X: float =0, STARTING_VEL_Y: float =0, FALLS: bool =False, PERSISTENT: bool =False) -> None:
        self.game = game
        
        self.BLOCK_TYPE = BLOCK_TYPE
        self.FALLS = FALLS
        
        self._x = STARTING_X
        self._y = STARTING_Y

        self._x_prev = self.x
        self._y_prev = self.y
        

        self.vel_x = STARTING_VEL_X
        self.vel_y = STARTING_VEL_Y

        self.SPRITE_X, self.SPRITE_Y, self.WIDTH, self.TALLNESS = BLOCK_TYPE.value

        self.PERSISTENT = PERSISTENT
        self.alive = True
    
    @property
    def x(self) -> float:
        return self._x
    @x.setter
    def x(self, value: float) -> None:
        self._x_prev = self._x
        self._x = value

    @property
    def y(self) -> float:
        return self._y
    @y.setter
    def y(self, value: float) -> None:
        self._y_prev = self._y
        self._y = min(value, FLOOR_HEIGHT - self.TALLNESS) # TODO: create a dynamic floor height with collisions

    # Only call super().update() on Entities that can move
    def update(self, jump=False) -> None:
        # X-AXIS air friction, so speed reduces naturally
        self.vel_x *= 1 - AIR_FRICTION_COEFFICIENT
        # X-movement
        self.x += self.vel_x
        # Y-movement and gravity
        if self.FALLS and self.height():
            self.vel_y += GRAVITY
        elif jump:
            self.vel_y = MARIO_JUMPING_INITIAL_SPEED
        else:
            self.vel_y = 0
        self.y += self.vel_y
    
    def draw(self) -> None:
        pyxel.blt(
            self.x - self.game.x,
            self.y,
            0, # image map that we want to use
            self.SPRITE_X,
            self.SPRITE_Y,
            self.WIDTH,
            self.TALLNESS,
            12 # color, blue, so it becomes transparent
        )

    def height(self) -> float:
        return FLOOR_HEIGHT - self.TALLNESS - self.y
    
    def center(self) -> tuple:
        return self.x + ( self.WIDTH / 2 ), self.y + ( self.TALLNESS / 2 )

    def angle(self) -> float:
        return math.atan2(self.vel_y, self.vel_x)      
        
    def corners(self) -> tuple:
        return ((self.x, self.y), (self.x + self.WIDTH, self.y), (self.x, self.y + self.TALLNESS), (self.x + self.WIDTH, self.y + self.TALLNESS))
    
    def rect_func(self, x) -> float:
        p = (self.y - self._y_prev) / (self.x - self._x_prev)
        return self._y_prev + p * (x - self._x_prev)
    
    def rect_func_inv(self, y) -> float:
        p = (self.x - self._x_prev) / (self.y - self._y_prev)
        return self._x_prev + p * (y - self._y_prev)
    
    def collides(self, other) -> tuple[DIR]:
        collision_corner = [DIR.none]
        
        x_interval = Entity.Interval(self.x, self.x + self.WIDTH)
        y_interval = Entity.Interval(self.y, self.y + self.TALLNESS)
        for corner in other.corners():
            if x_interval.contains(corner[0]) and y_interval.contains(corner[1]):
                try:
                    collision_corner.remove(DIR.none)
                except:
                    pass
                vector = [p - c for (p, c) in (corner, self.center())]
                vector_magnitude = math.sqrt(sum([sub^2 for sub in vector]))
                vector_magnitude_one = [sub / vector_magnitude for sub in vector]
                return DIR(vector_magnitude)
                
                collision_corner.append(corner)
        return collision_corner

    
            
        

        if ((self.x <= corners[0][0] and corners[0][0] <= self.x + self.WIDTH) and 
            (self.y <= corners[0][1] and corners[0][1] <= self.y + self.TALLNESS)):
            col = True
            corner = DIR.up_left

        if ((self.x <= corners[1][0] and corners[1][0] <= self.x + self.WIDTH) and
            (self.y <= corners[1][1] and corners[1][1] <= self.y + self.TALLNESS)):
            col = True
            corner = DIR.up_right

        if ((self.x <= corners[2][0] and corners[2][0] <= self.x + self.WIDTH) and
            (self.y <= corners[2][1] and corners[2][1] <= self.y + self.TALLNESS)):
            col = True
            corner = DIR.down_left

        if ((self.x <= corners[3][0] and corners[3][0] <= self.x + self.WIDTH) and
            (self.y <= corners[3][1] and corners[3][1] <= self.y + self.TALLNESS)):
            col = True
            corner = DIR.down_right 

        return col, corner
    
    class Interval:
        def __init__(self, left: float, closed_left: bool, right: float, closed_right: bool, is_b_relative_not_absolute: bool) -> None:
            self.left = left
            self.closed_left = closed_left
            self.right = left + right if is_b_relative_not_absolute else right
            self.closed_right = closed_right
        
        def contains(self, *points: list[float]) -> list[float]:
            contained_points = []
            for p in points:
                if self._contains_point(p):
                    contained_points.append(p)
            return contained_points

        def _contains_point(self, p: float) -> bool:
            return (
                (
                    (self.closed_left and self.left <= p)
                    or
                    (not self.closed_left and self.left < p)
                )
                and
                (
                    (self.closed_right and p <= self.right)
                    or
                    (not self.closed_right and p < self.right)
                )
            )



class Block(Entity):
    def update(self) -> None:
        corners = self.game.mario.corners()
        side = DIR.none
        a = self.game.mario.angle()
        #print("Mario's angle is: ", a)
        if ((self.x <= corners[0][0] and corners[0][0] <= self.x + self.WIDTH) and 
            (self.y <= corners[0][1] and corners[0][1] <= self.y + self.TALLNESS)):
            if abs(a - math.radians(90)) < 10 ^(-3):
                side = DIR.down
            elif abs(a - math.radians(180)) < 10 ^(-3):
                side = DIR.right
            else:
                p = self.game.mario.rect_func(self.x)
                p_inv = self.game.mario.rect_func_inv(self.y)
                if self.y <= p and p <= self.y + self.TALLNESS:
                    side = DIR.right
                elif self.x <= p_inv and p_inv <= self.x + self.WIDTH:
                    side = DIR.down
                elif math.radians(135) <= a and a <= math.radians(180):
                    side = DIR.right
                else:
                    side = DIR.down

        if ((self.x <= corners[1][0] and corners[1][0] <= self.x + self.WIDTH) and
            (self.y <= corners[1][1] and corners[1][1] <= self.y + self.TALLNESS)):
            if abs(a - math.radians(0)) < 10 ^(-3):
                side = DIR.left
            elif abs(a - math.radians(90)) < 10 ^(-3):
                side = DIR.down
            else:
                p = self.game.mario.rect_func(self.x - self.game.mario.WIDTH)
                p_inv = self.game.mario.rect_func_inv(self.y) + self.game.mario.WIDTH
                if self.y <= p and p <= self.y + self.TALLNESS:
                    side = DIR.left
                if self.x <= p_inv and p_inv <= self.x + self.WIDTH:
                    side = DIR.down
                elif 0 <= a and a <= math.radians(45):
                    side = DIR.left
                else:
                    side = DIR.down

        if ((self.x <= corners[2][0] and corners[2][0] <= self.x + self.WIDTH) and
            (self.y <= corners[2][1] and corners[2][1] <= self.y + self.TALLNESS)):
            if abs(a - math.radians(180)) < 10 ^(-3):
                side = DIR.right
            elif abs(a - math.radians(-90)) < 10 ^(-3):
                side = DIR.up
            else:
                p = self.game.mario.rect_func(self.x) + self.game.mario.TALLNESS
                p_inv = self.game.mario.rect_func_inv(self.y - self.game.mario.TALLNESS)
                if self.y <= p and p <= self.y + self.TALLNESS:
                    side = DIR.right
                if self.x <= p_inv and p_inv <= self.x + self.WIDTH:
                    side = DIR.up
                elif math.radians(-180) <= a and a <= math.radians(-135):
                    side = DIR.right
                else:
                    side = DIR.up

        if ((self.x <= corners[3][0] and corners[3][0] <= self.x + self.WIDTH) and
            (self.y <= corners[3][1] and corners[3][1] <= self.y + self.TALLNESS)):
            if abs(a - math.radians(0)) < 10 ^(-3):
                side = DIR.left
            elif abs(a - math.radians(-90)) < 10 ^(-3):
                side = DIR.up
            else:
                p = self.game.mario.rect_func(self.x - self.game.mario.WIDTH) + self.game.mario.TALLNESS
                p_inv = self.game.mario.rect_func_inv(self.y - self.game.mario.TALLNESS) + self.game.mario.WIDTH
                if self.y <= p and p <= self.y + self.TALLNESS:
                    side = DIR.left
                if self.x <= p_inv and p_inv <= self.x + self.WIDTH:
                    side = DIR.up
                elif math.radians(-180) <= a and a <= math.radians(-135):
                    side = DIR.left
                else:
                    side = DIR.up
                    
        if side != DIR.none:
            print("COLLISION DETECTED!!! from", side.name)
        else:
            pass #print("Not anymore")

        """col_dir = self.collides(self.game.mario.corners())
        con_1 = col_dir != DIR.none
        if con_1:
            print(col_dir.value, DIR.up.value, np.dot(col_dir.value, DIR.up.value))
        con_2 = np.dot(col_dir.value, DIR.up.value) > np.cos(math.radians(45))
        if con_1 and con_2:
            self.destroy(self.game)"""  # THIS WHOLE THING IS KINDA BS, NEEDS A REWRITE !!!
        
        super().update()


class Brick(Block):
    def __init__(self, game, STARTING_X, STARTING_Y, STARTING_VEL_X=0, STARTING_VEL_Y=0, FALLS=False, PERSISTENT=False) -> None:
        super().__init__(game, BLOCK_TYPES.brick, STARTING_X, STARTING_Y, STARTING_VEL_X=STARTING_VEL_X, STARTING_VEL_Y=STARTING_VEL_Y, FALLS=FALLS, PERSISTENT=PERSISTENT)


class Question_Brick(Block):
    def __init__(self, game, STARTING_X, STARTING_Y, STARTING_VEL_X=0, STARTING_VEL_Y=0, FALLS=False, PERSISTENT=False) -> None:
        super().__init__(game, BLOCK_TYPES.question_brick, STARTING_X, STARTING_Y, STARTING_VEL_X=STARTING_VEL_X, STARTING_VEL_Y=STARTING_VEL_Y, FALLS=FALLS, PERSISTENT=PERSISTENT)


class Clear_Brick(Block):
    def __init__(self, game, STARTING_X, STARTING_Y, STARTING_VEL_X=0, STARTING_VEL_Y=0, FALLS=False, PERSISTENT=False) -> None:
        super().__init__(game, BLOCK_TYPES.clear_brick, STARTING_X, STARTING_Y, STARTING_VEL_X=STARTING_VEL_X, STARTING_VEL_Y=STARTING_VEL_Y, FALLS=FALLS, PERSISTENT=PERSISTENT)


class Pipe():
    """
    Pipe is a complex object which cannot be directly rendered.
    That's why it's not an Entity.
    Despite this, all of its parts are Entities
    """
    def __init__(self, game, STARTING_X: float, STARTING_Y: float, STARTING_VEL_X: float =0, STARTING_VEL_Y: float =0, HEIGHT: float =0, FALLS: bool =False, PERSISTENT: bool =False) -> None:
        self.HEIGHT = 0
        if HEIGHT > 0:
            self.HEIGHT = HEIGHT
            self.parts = []

            self.parts.append(Pipe.Head(STARTING_X, STARTING_Y, STARTING_VEL_X, STARTING_VEL_Y, FALLS, PERSISTENT))
            
            for i in range(1, int(HEIGHT)):
                self.parts.append(Pipe.Body(STARTING_X, STARTING_Y + 16 * i, STARTING_VEL_X, STARTING_VEL_Y, FALLS, PERSISTENT))
            
            if self.HEIGHT - int(HEIGHT):
                self.parts.append(Pipe.Half_Body(STARTING_X, STARTING_Y + 16 * int(HEIGHT), STARTING_VEL_X, STARTING_VEL_Y, FALLS, PERSISTENT))

    def update(self) -> None:
        if self.HEIGHT > 0:
            [e.update() for e in self.parts]
    
    def draw(self) -> None:
        if self.HEIGHT > 0:
            [e.draw() for e in self.parts]
    
    class Head(Entity):
        def __init__(self, game, STARTING_X, STARTING_Y, STARTING_VEL_X=0, STARTING_VEL_Y=0, FALLS=False, PERSISTENT=False) -> None:
            super().__init__(game, BLOCK_TYPES.pipe_head, STARTING_X, STARTING_Y, STARTING_VEL_X=STARTING_VEL_X, STARTING_VEL_Y=STARTING_VEL_Y, FALLS=FALLS, PERSISTENT=PERSISTENT)


    class Body(Entity):
        def __init__(self, game, STARTING_X, STARTING_Y, STARTING_VEL_X=0, STARTING_VEL_Y=0, FALLS=False, PERSISTENT=False) -> None:
            super().__init__(game, BLOCK_TYPES.pipe_body, STARTING_X, STARTING_Y, STARTING_VEL_X=STARTING_VEL_X, STARTING_VEL_Y=STARTING_VEL_Y, FALLS=FALLS, PERSISTENT=PERSISTENT)
    

    class Half_Body(Entity):
        def __init__(self, game, STARTING_X, STARTING_Y, STARTING_VEL_X=0, STARTING_VEL_Y=0, FALLS=False, PERSISTENT=False) -> None:
            super().__init__(game, BLOCK_TYPES.pipe_half_body, STARTING_X, STARTING_Y, STARTING_VEL_X=STARTING_VEL_X, STARTING_VEL_Y=STARTING_VEL_Y, FALLS=FALLS, PERSISTENT=PERSISTENT)


class Cloud(Entity):
    starting = STARTING_DECORS
    def __init__(self, game, STARTING_X, STARTING_Y, STARTING_VEL_X=0, STARTING_VEL_Y=0, FALLS=False, PERSISTENT=False) -> None:
        super().__init__(game, BLOCK_TYPES.cloud, STARTING_X, STARTING_Y, STARTING_VEL_X=STARTING_VEL_X, STARTING_VEL_Y=STARTING_VEL_Y, FALLS=FALLS, PERSISTENT=PERSISTENT)


class Enemy(Entity):
    pass


class Goomba(Enemy):
    starting = STARTING_GOOMBAS
    def __init__(self, game, STARTING_X, STARTING_Y, STARTING_VEL_X=0, STARTING_VEL_Y=0, FALLS=False, PERSISTENT=False) -> None:
        super().__init__(game, BLOCK_TYPES.goomba, STARTING_X, STARTING_Y, STARTING_VEL_X=STARTING_VEL_X, STARTING_VEL_Y=STARTING_VEL_Y, FALLS=FALLS, PERSISTENT=PERSISTENT)


class Mushroom(Entity):
    def update(self) -> None:

        col, side = self.collides(self.game.mario.corners())
        if col:
            print("COLLISION DETECTED!!!")
        con_1 = side != DIR.none
        if con_1:
            print(side.value, DIR.up.value, np.dot(side.value, DIR.up.value))
        con_2 = True
        if con_1 and con_2:
            pass
        pyxel.quit()
        print("EEEEEEEEEE" * 10000)

        s = """ def dir(self) -> DIR:
        vel_x = self.vel_x
        vel_y = self.vel_y
        dir = None

        if vel_x > 0:
            if vel_y > 0:
                dir = DIR.down_right
            elif vel_y == 0:
                dir = DIR.right
            else:
                dir = DIR.up_right
        elif vel_x == 0:
            if vel_y > 0:
                dir = DIR.down
            elif vel_y == 0:
                dir = DIR.none
            else:
                dir = DIR.up
        else:
            if vel_y > 0:
                dir = DIR.down_left
            elif vel_y == 0:
                dir = DIR.left
            else:
                dir = DIR.up_left
        
        return dir """

        super().update()