import pyxel
import Solid
from Helper import DIR as DIR

class Mario(Solid):
    def __init__(self, PLAYER_STARTING_X, PLAYER_STARTING_Y, PLAYER_CONSTANT_VEL_X, PLAYER_STARTING_VEL_Y, BACKGROUND_RIGHT_MOVEMENT_THRESHOLD, FLOOR_HEIGHT, PLAYER_TALLNESS, PLAYER_WIDTH, GRAVITY, JUMPING_COEFFICIENT) -> None:
        self.x = PLAYER_STARTING_X
        self.y = PLAYER_STARTING_Y
        self.PLAYER_CONSTANT_VEL_X = PLAYER_CONSTANT_VEL_X
        self.vel_x = 0
        self.vel_y = PLAYER_STARTING_VEL_Y
        self.vel = DIR.up_right
        self.BACKGROUND_RIGHT_MOVEMENT_THRESHOLD = BACKGROUND_RIGHT_MOVEMENT_THRESHOLD
        self.FLOOR_HEIGHT = FLOOR_HEIGHT
        self.PLAYER_TALLNESS = PLAYER_TALLNESS
        self.PLAYER_WIDTH = PLAYER_WIDTH
        self.GRAVITY = GRAVITY
        self.JUMPING_COEFFICIENT = JUMPING_COEFFICIENT
        self.points = 0
        self.coins = 0
        self.time = 0
        self.jumps_pending = 0
        self.alive = True

    def update(self, game) -> bool: # returns True if the Mario moves and the Background has to move
        move_right = False

        # LEFT & RIGHT
        if pyxel.btnp(pyxel.KEY_RIGHT, 1, 1):
            self.vel_x = self.PLAYER_CONSTANT_VEL_X
            self.x = min(self.x + self.vel_x, self.BACKGROUND_RIGHT_MOVEMENT_THRESHOLD)
            move_right = True
        else:
            self.vel_x = 0
        if pyxel.btnp(pyxel.KEY_LEFT, 1, 1):
            self.vel_x = - self.PLAYER_CONSTANT_VEL_X
            self.x = max(self.x - self.vel_x, 0)
        else:
            self.vel_x = 0

        # JUMP, it is comprised of "mini-launches", each one linearly weaker than the last
        if pyxel.btnp(pyxel.KEY_UP):
            if self.height() == 0:
                self.jumps_pending = 10
        if self.jumps_pending != 0:
            self.vel_y -= self.JUMPING_COEFFICIENT * self.jumps_pending
            self.jumps_pending -= 1

        # Y-movement and gravity
        self.y = min(self.y + self.vel_y, self.FLOOR_HEIGHT - self.PLAYER_TALLNESS)
        self.vel_y = self.vel_y + self.GRAVITY if self.height() > 0 else 0

        self.vel = self.dir()

        return move_right
    
    def draw(self):
        # draw player
        pyxel.blt(
            self.x,
            self.y,
            0,
            0,
            48,
            16,
            16,
            12
        )
    
    def height(self) -> float:
        return self.FLOOR_HEIGHT - self.PLAYER_TALLNESS - self.y
    
    def dir(self) -> DIR:
        x = self.vel_x
        y = self.vel_y
        if x >= 0:
            if y >= 0:
                return DIR.up_down
            else:
                return DIR.up_right
        else:
            if y >= 0:
                return DIR.down_left
            else:
                return DIR.up_left
