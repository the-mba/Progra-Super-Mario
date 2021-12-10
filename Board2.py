from random import randint

import pyxel

PLAYER_STARTING_X = 40
PLAYER_STARTING_Y = 82
PLAYER_STARTING_VEL_Y = 0
GRAVITY = 0.4

PLAYER_TALLNESS = 16
WIDTH = 160
HEIGHT = 120
FLOOR_HEIGHT = HEIGHT - 22

class App:
    def __init__(self):
        pyxel.init(WIDTH, HEIGHT, caption="Pyxel Jump")

        pyxel.load("assets/marioassets_133.pyxres")

        self.score = 0
        self.player_x = PLAYER_STARTING_X
        self.player_y = PLAYER_STARTING_Y
        self.player_vel_y = PLAYER_STARTING_VEL_Y
        self.player_alive = True
        self.jumps_pending = 0

        pyxel.playm(0, loop=True)

        pyxel.run(self.update, self.draw)

    def height(self):
        return FLOOR_HEIGHT - PLAYER_TALLNESS - self.player_y

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        
        self.update_player()

    def update_player(self):
        if pyxel.btnp(pyxel.KEY_RIGHT, 1, 1):
            self.player_x = min(self.player_x + 2, pyxel.width - 16)
        if pyxel.btnp(pyxel.KEY_LEFT, 1, 1):
            self.player_x = max(self.player_x - 2, 0)
        if pyxel.btnp(pyxel.KEY_UP):
            if self.height() == 0:
                self.jumps_pending = 10

        if self.jumps_pending != 0:
            self.player_vel_y -= 0.1 * self.jumps_pending
            self.jumps_pending -= 1

        self.player_y = min(self.player_y + self.player_vel_y, FLOOR_HEIGHT - PLAYER_TALLNESS)
        self.player_vel_y = self.player_vel_y + GRAVITY if self.height() > 0 else 0

    def draw(self):
        pyxel.cls(12)

        # draw sky
        pyxel.bltm(0, 50, 0, 0, 88, 160, 32)
        pyxel.tilemap(0)

        # draw player
        pyxel.blt(
            self.player_x,
            self.player_y,
            0,
            0 if self.player_vel_y > 0 else 0,
            48,
            16,
            16,
            12
        )

        # draw score
        s = "SCORE {:>4}".format(self.player_vel_y)
        pyxel.text(5, 4, s, 1)
        pyxel.text(4, 4, s, 7)


App()
