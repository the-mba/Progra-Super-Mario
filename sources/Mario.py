import pyxel
from Entity import Entity
from Helper import *

class Mario(Entity):
    def __init__(self, game) -> None:
        super().__init__(game, BLOCK_TYPES.mario, MARIO_STARTING_X, MARIO_STARTING_Y, MARIO_STARTING_VEL_X, MARIO_STARTING_VEL_Y, FALLS=True, PERSISTENT=True)
        self.effects = []
        
        self.points = 0
        self.coins = 0
        self.time = 0
        
    @property
    def x(self) -> float:
        return self._x
    @x.setter
    def x(self, value: float):
        self._x_prev = self._x
        self._x = max(value, self.game.x)

    def update(self) -> float:
        move_right = 0 # if bigger than 0, both Mario and the background need to be moved this much
        jump = False

        # RIGHT
        if pyxel.btnp(pyxel.KEY_RIGHT, 1, 1):
            self.vel_x += MARIO_ACC_X
        # LEFT
        if pyxel.btnp(pyxel.KEY_LEFT, 1, 1):
            self.vel_x -= MARIO_ACC_X

        move_right = max ( (self.x + self.vel_x) - (self.game.x + BACKGROUND_RIGHT_MOVEMENT_THRESHOLD), 0 )
        if DEBUG:
            print(f'{self.vel_x = }')
            print(f'{move_right = }')
        
        

        super().update(jump= pyxel.btnp(pyxel.KEY_UP) and not self.height())

        return move_right