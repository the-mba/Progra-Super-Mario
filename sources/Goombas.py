import pyxel
import Solid

class Goombas:
    def __init__(self) -> None:
        self.list = []
    
    def draw(self) -> None:
        for goomba in self.list:
            goomba.draw()

    def new(self, STARTING_X, STARTING_Y,  STARTING_VEL_X, STARTING_VEL_Y,  WIDTH, TALLNESS,  SPRITE_X, SPRITE_Y,  FLOOR_HEIGHT):
        new_goomba = Goomba(STARTING_X, STARTING_Y,  STARTING_VEL_X, STARTING_VEL_Y,  WIDTH, TALLNESS,  SPRITE_X, SPRITE_Y,  FLOOR_HEIGHT)
        self.list.append(new_goomba)
        return new_goomba

class Goomba(Solid.Solid):
    def __init__(self, STARTING_X, STARTING_Y,  STARTING_VEL_X, STARTING_VEL_Y,  WIDTH, TALLNESS,  SPRITE_X, SPRITE_Y,  FLOOR_HEIGHT) -> None:
        super().__init__(STARTING_X, STARTING_Y,  STARTING_VEL_X, STARTING_VEL_Y,  WIDTH, TALLNESS,  SPRITE_X, SPRITE_Y,  FLOOR_HEIGHT)
    
    def update(self, mario_pos) -> bool:
        pass

    def draw(self) -> None:
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