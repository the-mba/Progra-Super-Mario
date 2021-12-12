import pyxel

class Goombas:
    def __init__(self) -> None:
        self.list = []

    class Goomba:
        def __init__(self, x, y, x_vel) -> None:
            self.x = x
            self.y = y
            self.x_vel = x_vel
        
        def update(self, mario_pos) -> bool:
            self.mario_x, self.mario_y = mario_pos

        def draw(self):
            pyxel.blt(
            self.x,
            self.y,
            0,
            32,
            48,
            16,
            16,
            12
        )