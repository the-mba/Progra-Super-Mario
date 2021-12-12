import pyxel

class Mario:
    def __init__(self, starting_x, starting_y) -> None:
        self.x = starting_x
        self.y = starting_y
        self.points = 0
        self.coins = 0
        self.time = 0
        self.jumps_pending = 0

    def update(self, game):
        # LEFT & RIGHT
        if pyxel.btnp(pyxel.KEY_RIGHT, 1, 1):
            self.player_x = min(self.player_x + PLAYER_VEL_X, pyxel.width - 16)
        if pyxel.btnp(pyxel.KEY_LEFT, 1, 1):
            self.player_x = max(self.player_x - PLAYER_VEL_X, 0)

        # JUMP, it is comprised of "mini-launches", each one linearly weaker than the last
        if pyxel.btnp(pyxel.KEY_UP):
            if self.height() == 0:
                self.mario.jumps_pending = 10
        if self.mario.jumps_pending != 0:
            self.player_vel_y -= 0.11 * self.mario.jumps_pending
            self.mario.jumps_pending -= 1

        # Y-movement and gravity
        self.player_y = min(self.player_y + self.player_vel_y, FLOOR_HEIGHT - PLAYER_TALLNESS)
        self.player_vel_y = self.player_vel_y + GRAVITY if self.height() > 0 else 0