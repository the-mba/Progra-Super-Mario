import pyxel

class Block:
    def __init__(self, starting_x, starting_y, width, height, starting_vel_x, starting_vel_y) -> None:
        self.x = starting_x
        self.y = starting_y
        self.width = width
        self.height = height
        self.vel_x = starting_vel_x
        self.vel_y = starting_vel_y

    def update(self, mario) -> None:
        pass

    def collision(self, mario) -> None:
        pass

    def contains(self, corners) -> None:
        return ( self.x <= corners[0][1]
        and corners[0][1] <= self.x + self.width )
        
        
    
    def corners(self) -> tuple:
        return ((self.x, self.y), (self.x + self.WIDTH, self.y), (self.x, self.y + self.PLAYER_TALLNESS), (self.x + self.WIDTH, self.y + self.PLAYER_TALLNESS))