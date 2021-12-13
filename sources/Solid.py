import pyxel
from Helper import DIR as DIR

class Solid:
    def __init__(self, STARTING_X, STARTING_Y,  STARTING_VEL_X, STARTING_VEL_Y,  WIDTH, TALLNESS,  SPRITE_X, SPRITE_Y,  FLOOR_HEIGHT) -> None:
        self.x = STARTING_X
        self.y = STARTING_Y

        self.vel_x = STARTING_VEL_X
        self.vel_y = STARTING_VEL_Y

        self.WIDTH = WIDTH
        self.TALLNESS = TALLNESS

        self.SPRITE_X = SPRITE_X
        self.SPRITE_Y = SPRITE_Y

        self.FLOOR_HEIGHT = FLOOR_HEIGHT
        self.vel = DIR.none
        self.alive = True

    def update(self, mario) -> None:
        pass

    def draw(self) -> None:
        pyxel.blt(
            self.x,
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