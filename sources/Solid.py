import pyxel
from Helper import DIR as DIR

class Block:
    def __init__(self, starting_x, starting_y, width, tallness, starting_vel_x, starting_vel_y, FLOOR_HEIGHT) -> None:
        self.x = starting_x
        self.y = starting_y
        self.width = width
        self.tallness = height
        self.vel_x = starting_vel_x
        self.vel_y = starting_vel_y
        self.FLOOR_HEIGHT = FLOOR_HEIGHT
        self.vel = DIR.none
        self.alive = True

    def update(self, mario) -> None:
        pass

    def draw(self) -> None:
        pass

    def height(self) -> float:
        return self.FLOOR_HEIGHT - self.tallness - self.y
    
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
        return ((self.x, self.y), (self.x + self.WIDTH, self.y), (self.x, self.y + self.PLAYER_TALLNESS), (self.x + self.WIDTH, self.y + self.PLAYER_TALLNESS))