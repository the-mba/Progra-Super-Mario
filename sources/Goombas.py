import pyxel
import Solid

class Goombas:
    def __init__(self, WIDTH) -> None:
        self.list = []
        self.WIDTH = WIDTH

    def update(self, mario) -> None:
        # Update the level moving forward, for drawing purposes
        for goomba in self.list:
            goomba.update(mario)
    
    def draw(self, level_x) -> None:
        for goomba in self.list:                
            goomba.draw(level_x)

    def new(self, STARTING_X, STARTING_Y,  STARTING_VEL_X, STARTING_VEL_Y,  WIDTH, TALLNESS,  SPRITE_X, SPRITE_Y, FLOOR_HEIGHT):
        new_goomba = Goomba(STARTING_X, STARTING_Y,  STARTING_VEL_X, STARTING_VEL_Y,  WIDTH, TALLNESS,  SPRITE_X, SPRITE_Y, False, FLOOR_HEIGHT)
        self.list.append(new_goomba)
        return new_goomba

class Goomba(Solid.Solid):
    def __init__(self, STARTING_X, STARTING_Y,  STARTING_VEL_X, STARTING_VEL_Y,  WIDTH, TALLNESS,  SPRITE_X, SPRITE_Y,  PERSISTENT, FLOOR_HEIGHT) -> None:
        super().__init__(STARTING_X, STARTING_Y,  STARTING_VEL_X, STARTING_VEL_Y,  WIDTH, TALLNESS,  SPRITE_X, SPRITE_Y,  PERSISTENT, FLOOR_HEIGHT)
    
    def update(self, mario) -> bool:
        pass