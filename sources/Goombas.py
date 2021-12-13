import pyxel
import Solid

class Goombas:
    def __init__(self, WIDTH) -> None:
        self.list = []
        self.WIDTH = WIDTH

    def update(self, level_x, mario) -> None:
        # Update the level moving forward, for drawing purposes
        for goomba in self.list:
            goomba.update(level_x, mario)
    
    def draw(self) -> None:
        for goomba in self.list:
            if goomba.level_x - goomba.WIDTH <= goomba.x and goomba.x <= goomba.level_x + self.WIDTH:
                goomba.draw()

    def new(self, STARTING_X, STARTING_Y,  STARTING_VEL_X, STARTING_VEL_Y,  WIDTH, TALLNESS,  SPRITE_X, SPRITE_Y,  FLOOR_HEIGHT):
        new_goomba = Goomba(STARTING_X, STARTING_Y,  STARTING_VEL_X, STARTING_VEL_Y,  WIDTH, TALLNESS,  SPRITE_X, SPRITE_Y,  FLOOR_HEIGHT)
        self.list.append(new_goomba)
        return new_goomba

class Goomba(Solid.Solid):
    def __init__(self, STARTING_X, STARTING_Y,  STARTING_VEL_X, STARTING_VEL_Y,  WIDTH, TALLNESS,  SPRITE_X, SPRITE_Y,  FLOOR_HEIGHT) -> None:
        super().__init__(STARTING_X, STARTING_Y,  STARTING_VEL_X, STARTING_VEL_Y,  WIDTH, TALLNESS,  SPRITE_X, SPRITE_Y,  FLOOR_HEIGHT)
    
    def update(self, level_x, mario) -> bool:
        # Update the level moving forward, for drawing purposes
        self.level_x = level_x

    def draw(self) -> None:
        print(f"{self.x=} {self.level_x=}")
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