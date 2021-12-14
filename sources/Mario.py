import pyxel
from Entity import Entity
from Helper import *

class Mario(Entity):

    def __init__(self) -> None:
        super().__init__(BLOCK_TYPES.mario, MARIO_STARTING_X, MARIO_STARTING_Y, 0, MARIO_STARTING_VEL_Y, False, True)

        self.previous_x = MARIO_STARTING_X
        self.previous_y = MARIO_STARTING_Y

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
            self.previous_x = self.x
            self.x += self.vel_x
            if self.x >= level_x + BACKGROUND_RIGHT_MOVEMENT_THRESHOLD:
                self.x = level_x + BACKGROUND_RIGHT_MOVEMENT_THRESHOLD + 8
            move_right = True
        else:
            self.vel_x = 0
        # LEFT
        if pyxel.btnp(pyxel.KEY_LEFT, 1, 1):
            self.vel_x = -MARIO_CONSTANT_VEL_X
            self.previous_x = self.x
            self.x = max(self.x + self.vel_x, level_x)
        else:
            self.vel_x = 0

        # JUMP, a starting speed and then gravity
        if pyxel.btnp(pyxel.KEY_UP):
            if self.height() == 0:
                self.vel_y -= MARIO_JUMPING_INITIAL_SPEED

        return move_right and self.x >= level_x + BACKGROUND_RIGHT_MOVEMENT_THRESHOLD
    
    
