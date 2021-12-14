import pyxel
import Solid
from Helper import *

class Mario(Solid.Solid):

    def __init__(self, MARIO_STARTING_X, MARIO_STARTING_Y, MARIO_STARTING_VEL_Y, PERSISTENT) -> None:
        super().__init__(BLOCK_TYPES.mario, MARIO_STARTING_X, MARIO_STARTING_Y, 0, MARIO_STARTING_VEL_Y, 1, True)

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
            self.x += self.vel_x
            if self.x >= level_x + BACKGROUND_RIGHT_MOVEMENT_THRESHOLD:
                self.x = level_x + BACKGROUND_RIGHT_MOVEMENT_THRESHOLD + 8
            move_right = True
        else:
            self.vel_x = 0
        # LEFT
        if pyxel.btnp(pyxel.KEY_LEFT, 1, 1):
            self.vel_x = -MARIO_CONSTANT_VEL_X
            self.x = max(self.x + self.vel_x, level_x)
        else:
            self.vel_x = 0

        # JUMP, it is comprised of "mini-launches", each one linearly weaker than the last
        if pyxel.btnp(pyxel.KEY_UP):
            if self.height() == 0:
                self.jumps_pending = 3
        if self.jumps_pending != 0:
            self.vel_y -= JUMPING_COEFFICIENT * self.jumps_pending
            self.jumps_pending -= 1

        return move_right and self.x >= level_x + BACKGROUND_RIGHT_MOVEMENT_THRESHOLD
    
    
