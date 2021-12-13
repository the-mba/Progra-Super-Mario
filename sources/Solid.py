import pyxel
import Solid
from Helper import DIR as DIR
from Helper import BLOCK_TYPES
from My_Collection import My_Collection

class Solid:
    def __init__(self, BLOCK_TYPE, STARTING_X, STARTING_Y, STARTING_VEL_X, STARTING_VEL_Y, FLOOR_HEIGHT, HEIGHT=1, PERSISTENT=False) -> None:
        self.x = STARTING_X
        self.y = STARTING_Y

        self.vel_x = STARTING_VEL_X
        self.vel_y = STARTING_VEL_Y

        self.SPRITE_X, self.SPRITE_Y, self.WIDTH, self.TALLNESS = BLOCK_TYPE.value

        self.PERSISTENT = PERSISTENT
        self.FLOOR_HEIGHT = FLOOR_HEIGHT
        self.vel = DIR.none
        self.alive = True

    def update(self, mario) -> None:
        pass

    def draw(self, level_x) -> None:
        pyxel.blt(
            self.x - level_x,
            self.y,
            0, # image map that we want to use
            self.SPRITE_X,
            self.SPRITE_Y,
            self.WIDTH,
            self.TALLNESS,
            12 # color, blue, so it becomes transparent
        )

    def height(self) -> float:
        return max(0, self.FLOOR_HEIGHT - self.TALLNESS - self.y)
    
    def dir(self) -> DIR:
        x = self.vel_x
        y = self.vel_y
        if x >= 0:
            if y >= 0:
                return DIR.down_right
            else:
                return DIR.up_right
        else:
            if y >= 0:
                return DIR.down_left
            else:
                return DIR.up_left

    def collides(self, corners) -> DIR:
        side = DIR.none

        if ((self.x <= corners[0][0] and corners[0][0] <= self.x + self.width) and 
            (self.y <= corners[0][1] and corners[0][1] <= self.y + self.height)):
            side = DIR.up_left

        if ((self.x <= corners[1][0] and corners[1][0] <= self.x + self.width) and
            (self.y <= corners[1][1] and corners[1][1] <= self.y + self.height)):
            side = DIR.up_right

        if ((self.x <= corners[2][0] and corners[2][0] <= self.x + self.width) and
            (self.y <= corners[2][1] and corners[2][1] <= self.y + self.height)):
            side = DIR.down_left

        if ((self.x <= corners[3][0] and corners[3][0] <= self.x + self.width) and
            (self.y <= corners[3][1] and corners[3][1] <= self.y + self.height)):
            side = DIR.down_right 

        return side         
        
    def corners(self) -> tuple:
        return ((self.x, self.y), (self.x + self.WIDTH, self.y), (self.x, self.y + self.MARIO_TALLNESS), (self.x + self.WIDTH, self.y + self.MARIO_TALLNESS))


class Block(Solid):
    s = """
    def __init__(self, BLOCK_TYPE, STARTING_X, STARTING_Y, STARTING_VEL_X, STARTING_VEL_Y, FLOOR_HEIGHT, HEIGHT, PERSISTENT=False) -> None:
        super().__init__(BLOCK_TYPE, STARTING_X, STARTING_Y, STARTING_VEL_X, STARTING_VEL_Y, FLOOR_HEIGHT, HEIGHT, PERSISTENT=False)"""


class Goomba(Solid):
    def __init__(self, BLOCK_TYPE, STARTING_X, STARTING_Y, STARTING_VEL_X, STARTING_VEL_Y, HEIGHT, FLOOR_HEIGHT, PERSISTENT=False) -> None:
        super().__init__(BLOCK_TYPE, STARTING_X, STARTING_Y, STARTING_VEL_X, STARTING_VEL_Y, FLOOR_HEIGHT, HEIGHT, PERSISTENT=False)


class Pipe():
    def __init__(self, BLOCK_TYPE, STARTING_X, STARTING_Y, STARTING_VEL_X, STARTING_VEL_Y, FLOOR_HEIGHT, HEIGHT=2, PERSISTENT=False) -> None:
        self.parts = My_Collection(Pipe.Part)
        self.HEIGHT = HEIGHT
        self.parts.new(BLOCK_TYPES.pipe_head, STARTING_X, STARTING_Y, STARTING_VEL_X, STARTING_VEL_Y, FLOOR_HEIGHT, HEIGHT, PERSISTENT)
        for i in range(1, HEIGHT):
            self.parts.new(BLOCK_TYPES.pipe_body, STARTING_X, STARTING_Y + 16 * i, STARTING_VEL_X, STARTING_VEL_Y, FLOOR_HEIGHT, HEIGHT, PERSISTENT)
    
    def update(self, mario) -> None:
        self.parts.update(mario)
    
    def draw(self, level_x) -> None:
        self.parts.draw(level_x)
    
    class Part(Solid):
        def __init__(self, BLOCK_TYPE, STARTING_X, STARTING_Y, STARTING_VEL_X, STARTING_VEL_Y, FLOOR_HEIGHT, HEIGHT, PERSISTENT=False) -> None:
            super().__init__(BLOCK_TYPE, STARTING_X, STARTING_Y, STARTING_VEL_X, STARTING_VEL_Y, FLOOR_HEIGHT)
        