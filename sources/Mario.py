import pyxel
from Entity import Entity
from Helper import *

class Mario(Entity):

    def __init__(self, game) -> None:  # BLOCK_TYPES.mario, MARIO_STARTING_X, MARIO_STARTING_Y, 0, MARIO_STARTING_VEL_Y, False, True
        super().__init__(BLOCK_TYPES.mario, MARIO_STARTING_X, MARIO_STARTING_Y, 0, MARIO_STARTING_VEL_Y, 1, True, True)
        self.game = game
        self.effects = []
        self.points = 0
        self.coins = 0
        self.time = 0
        self.jumps_pending = 0
        self.x_extra = 0  # as the background can only move in 8 by 8 steps, we accumulate Mario's extra movement and when it reaches 8 we advance a background tile. Mario can never move more to the right than its supposed position, even if the background doesn't move

    @property
    def x(self):
        return self._x
    @x.setter
    def x(self, value):
        self._x_prev = self._x
        self._x = min( max(value, self.game.x), self.game.x + BACKGROUND_RIGHT_MOVEMENT_THRESHOLD )

    def update(self) -> bool: # returns True if the Mario moves and the Background has to move
        move_right = 0

        # RIGHT
        if pyxel.btnp(pyxel.KEY_RIGHT, 1, 1):
            self.vel_x = min ( self.vel_x + MARIO_CONSTANT_VEL_X, MARIO_CONSTANT_VEL_X )
            delta = (self.x + self.vel_x) - self.game.x - BACKGROUND_RIGHT_MOVEMENT_THRESHOLD
            if delta > 0:
                self.x = self.game.x + BACKGROUND_RIGHT_MOVEMENT_THRESHOLD
                self.vel_x = 0
                self.x_extra += delta
                move_right = self.x_extra // 8
                if move_right:
                    self.x_extra %= 8
        print(f'{self.x_extra=}')
        
        # LEFT
        if pyxel.btnp(pyxel.KEY_LEFT, 1, 1):
            self.vel_x = max ( self.vel_x + (-MARIO_CONSTANT_VEL_X), -MARIO_CONSTANT_VEL_X )
        
        # JUMP, a starting speed and then gravity
        if pyxel.btnp(pyxel.KEY_UP) and self.height() == 0:
                self.vel_y += MARIO_JUMPING_INITIAL_SPEED  

        
        super().update(self.game)   

        return move_right
    
    
    
