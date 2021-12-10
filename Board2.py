from random import randint

import pyxel

PLAYER_STARTING_X = 40
PLAYER_STARTING_Y = 82
PLAYER_STARTING_VEL_Y = 0
GRAVITY = 0.38

class App:
    def __init__(self):
        pyxel.init(160, 120, caption="Pyxel Jump")

        pyxel.load("assets/marioassets_133.pyxres")

        self.score = 0
        self.player_x = PLAYER_STARTING_X
        self.player_y = PLAYER_STARTING_Y
        self.player_vel_y = PLAYER_STARTING_VEL_Y
        self.player_alive = True

        pyxel.playm(0, loop=True)

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        
        self.update_player()

    def update_player(self):
        if pyxel.btnp(pyxel.KEY_RIGHT, 1, 1):
            self.player_x = min(self.player_x + 2, pyxel.width - 16)
        if pyxel.btnp(pyxel.KEY_LEFT, 1, 1):
            self.player_x = max(self.player_x - 2, 0)
        if pyxel.btnp(pyxel.KEY_UP, 1, 1):
            self.player_vel_y += -2
        
        self.player_y = max(self.player_y + self.player_vel_y, HEIGHT)
        self.player_vel_y += GRAVITY
        


        if self.player_y > pyxel.height:
            if self.player_alive:
                self.player_alive = False
                pyxel.play(3, 5)

            if self.player_y > 600:
                self.score = 0
                self.player_x = 72
                self.player_y = -16
                self.player_vy = 0
                self.player_alive = True

    def draw(self):
        pyxel.cls(12)

        # draw sky
        pyxel.bltm(0, 50, 0, 0, 88, 160, 32)

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
        s = "SCORE {:>4}".format(self.score)
        pyxel.text(5, 4, s, 1)
        pyxel.text(4, 4, s, 7)


App()
