import pyxel

class Mario:
    def __init__(self, PLAYER_STARTING_X, PLAYER_STARTING_Y, PLAYER_CONSTANT_VEL_X, PLAYER_STARTING_VEL_Y, FLOOR_HEIGHT, PLAYER_TALLNESS, GRAVITY, JUMPING_COEFFICIENT) -> None:
        self.x = PLAYER_STARTING_X
        self.y = PLAYER_STARTING_Y
        self.PLAYER_CONSTANT_VEL_X = PLAYER_CONSTANT_VEL_X
        self.vel_y = PLAYER_STARTING_VEL_Y
        self.FLOOR_HEIGHT = FLOOR_HEIGHT
        self.PLAYER_TALLNESS = PLAYER_TALLNESS
        self.GRAVITY = GRAVITY
        self.JUMPING_COEFFICIENT = JUMPING_COEFFICIENT
        self.points = 0
        self.coins = 0
        self.time = 0
        self.jumps_pending = 0
        self.alive = True

    def update(self, game) -> None:
        # LEFT & RIGHT
        if pyxel.btnp(pyxel.KEY_RIGHT, 1, 1):
            self.x = min(self.x + self.PLAYER_CONSTANT_VEL_X, pyxel.width - 16)
        if pyxel.btnp(pyxel.KEY_LEFT, 1, 1):
            self.x = max(self.x - self.PLAYER_CONSTANT_VEL_X, 0)

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