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

    def update(self, game) -> bool: # returns True if the Mario moves and the Background has to move
        move_right = 0

        # RIGHT
        if pyxel.btnp(pyxel.KEY_RIGHT, 1, 1):
            self.vel_x = MARIO_CONSTANT_VEL_X
            delta = self.x + self.vel_x - game.x - BACKGROUND_RIGHT_MOVEMENT_THRESHOLD
            if delta > 0:
                self.x = game.x + BACKGROUND_RIGHT_MOVEMENT_THRESHOLD
                move_right = delta
        
        # LEFT
        if pyxel.btnp(pyxel.KEY_LEFT, 1, 1):
            self.vel_x = -MARIO_CONSTANT_VEL_X
            self.x = max(self.x + self.vel_x, game.x)
        
        # JUMP, a starting speed and then gravity
        if pyxel.btnp(pyxel.KEY_UP):
            if self.height() == 0:
                self.vel_y -= MARIO_JUMPING_INITIAL_SPEED  

        
        super().update(game)     

        return move_right
    
    
    
