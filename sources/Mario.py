import pyxel
from Entity import Entity
from Helper import *

class Mario(Entity):

    def __init__(self, game) -> None:  # BLOCK_TYPES.mario, MARIO_STARTING_X, MARIO_STARTING_Y, 0, MARIO_STARTING_VEL_Y, False, True
        super().__init__(game, BLOCK_TYPES.mario, MARIO_STARTING_X, MARIO_STARTING_Y, 0, MARIO_STARTING_VEL_Y, 1, True, True)
        self._vel_x = 0
        self.effects = []
        self.points = 0
        self.coins = 0
        self.time = 0
        self.jumps_pending = 0
        
    @property
    def x(self):
        return self._x
    @x.setter
    def x(self, value):
        self._x_prev = self._x
        self._x = min( max(value, self.game.x), self.game.x + BACKGROUND_RIGHT_MOVEMENT_THRESHOLD )
    
    @property
    def vel_x(self):
        return self._vel_x
    @vel_x.setter
    def vel_x(self, value):
        self._vel_x = min( max( value, -MARIO_CONSTANT_VEL_X), MARIO_CONSTANT_VEL_X)

    def update(self) -> int:
        move_right = 0

        # RIGHT
        if pyxel.btnp(pyxel.KEY_RIGHT, 1, 1):
            move_right = max ( (self.x + MARIO_CONSTANT_VEL_X) - (self.game.x + BACKGROUND_RIGHT_MOVEMENT_THRESHOLD), 0 )
            print(f'{move_right=}')
            self.vel_x = move_right if move_right else MARIO_CONSTANT_VEL_X
        
        # LEFT
        if pyxel.btnp(pyxel.KEY_LEFT, 1, 1):
            self.vel_x -= MARIO_CONSTANT_VEL_X
        
        # JUMP, a starting speed and then gravity
        if pyxel.btnp(pyxel.KEY_UP) and self.height() == 0:
            self.vel_y += MARIO_JUMPING_INITIAL_SPEED  

        
        super().update()   

        return move_right
    
    
    
