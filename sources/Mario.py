import pyxel
import Solid
from Helper import DIR as DIR

class Mario(Solid.Solid):

    def __init__(self, MARIO_STARTING_X, MARIO_STARTING_Y, MARIO_CONSTANT_VEL_X, MARIO_STARTING_VEL_Y, MARIO_WIDTH, MARIO_TALLNESS, MARIO_SPRITE_X, MARIO_SPRITE_Y, FLOOR_HEIGHT, BACKGROUND_RIGHT_MOVEMENT_THRESHOLD, GRAVITY, JUMPING_COEFFICIENT) -> None:
        super().__init__(MARIO_STARTING_X, MARIO_STARTING_Y, 0, MARIO_STARTING_VEL_Y, MARIO_WIDTH, MARIO_TALLNESS, MARIO_SPRITE_X, MARIO_SPRITE_Y, FLOOR_HEIGHT)
        
        self.MARIO_CONSTANT_VEL_X = MARIO_CONSTANT_VEL_X
        self.BACKGROUND_RIGHT_MOVEMENT_THRESHOLD = BACKGROUND_RIGHT_MOVEMENT_THRESHOLD
        self.FLOOR_HEIGHT = FLOOR_HEIGHT
        self.GRAVITY = GRAVITY
        self.JUMPING_COEFFICIENT = JUMPING_COEFFICIENT
        self.points = 0
        self.coins = 0
        self.time = 0
        self.jumps_pending = 0

    def update(self, game) -> bool: # returns True if the Mario moves and the Background has to move
        move_right = False
        level_x = game.gui.background.x

        # RIGHT
        if pyxel.btnp(pyxel.KEY_RIGHT, 1, 1):
            self.vel_x = self.MARIO_CONSTANT_VEL_X
            self.x = min(self.x + self.vel_x, level_x + self.BACKGROUND_RIGHT_MOVEMENT_THRESHOLD)
            move_right = True
        else:
            self.vel_x = 0
        # LEFT
        if pyxel.btnp(pyxel.KEY_LEFT, 1, 1):
            self.vel_x = -self.MARIO_CONSTANT_VEL_X
            self.x = max(self.x + self.vel_x, level_x)
        else:
            self.vel_x = 0

        # JUMP, it is comprised of "mini-launches", each one linearly weaker than the last
        if pyxel.btnp(pyxel.KEY_UP):
            if self.height() == 0:
                self.jumps_pending = 3
        if self.jumps_pending != 0:
            self.vel_y -= self.JUMPING_COEFFICIENT * self.jumps_pending
            self.jumps_pending -= 1

        # Y-movement and gravity
        self.y = min(self.y + self.vel_y, self.FLOOR_HEIGHT - self.TALLNESS)
        self.vel_y = self.vel_y + self.GRAVITY if self.height() > 0 else 0

        self.vel = self.dir()

        return move_right and self.x == level_x + self.BACKGROUND_RIGHT_MOVEMENT_THRESHOLD
    
    
