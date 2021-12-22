import pyxel
from Entity import Entity
from Helper import *

class Mario(Entity):

    def __init__(self) -> None:  # BLOCK_TYPES.mario, MARIO_STARTING_X, MARIO_STARTING_Y, 0, MARIO_STARTING_VEL_Y, False, True
        super().__init__(BLOCK_TYPES.mario, MARIO_STARTING_X, MARIO_STARTING_Y, 0, MARIO_STARTING_VEL_Y, 1, True, True)

        self.effects = []
        self.points = 0
        self.coins = 0
        self.time = 0
        self.jumps_pending = 0

    def update(self, level_x) -> bool: # returns True if the Mario moves and the Background has to move
        super().update(level_x)
        
        move_right = False

        # RIGHT
        if pyxel.btnp(pyxel.KEY_RIGHT, 1, 1):
            self.vel_x = MARIO_CONSTANT_VEL_X
            if self.x >= level_x + BACKGROUND_RIGHT_MOVEMENT_THRESHOLD:
                self.x = level_x + BACKGROUND_RIGHT_MOVEMENT_THRESHOLD + 8
            move_right = True
        
        # LEFT
        if pyxel.btnp(pyxel.KEY_LEFT, 1, 1):
            self.vel_x = -MARIO_CONSTANT_VEL_X
            self.x = max(self.x + self.vel_x, level_x)

        if self.vel_x != 0:
            vel_x_prev = self.vel_x
            vel_x_prev_abs = abs( vel_x_prev )

            vel_x_post_abs = max ( vel_x_prev_abs + MARIO_AIR_FRICTION, 0 )
            if vel_x_prev_abs > -MARIO_AIR_FRICTION:
                vel_x_post_abs = vel_x_prev_abs + MARIO_AIR_FRICTION
                vel_x_post = vel_x_post_abs * abs(vel_x_prev) / vel_x_prev
            else:
                vel_x_post = 0
            self.vel_x = vel_x_post
        
        # This could be moved to a method, like apply_vels(self)
        self.x += self.vel_x

        # JUMP, a starting speed and then gravity
        if pyxel.btnp(pyxel.KEY_UP):
            if self.height() == 0:
                self.vel_y -= MARIO_JUMPING_INITIAL_SPEED

        return move_right and self.x >= level_x + BACKGROUND_RIGHT_MOVEMENT_THRESHOLD
    
    
    
