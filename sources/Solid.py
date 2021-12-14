import pyxel
import numpy as np

import Solid
from Helper import *
from My_Collection import My_Collection

class Solid:
    def __init__(self, BLOCK_TYPE, STARTING_X, STARTING_Y, STARTING_VEL_X, STARTING_VEL_Y, HEIGHT=1, FALLS=False, PERSISTENT=False) -> None:
        self.BLOCK_TYPE = BLOCK_TYPE
        self.FALLS = FALLS
        
        self.x = STARTING_X
        self.y = STARTING_Y

        self.vel_x = STARTING_VEL_X
        self.vel_y = STARTING_VEL_Y

        self.SPRITE_X, self.SPRITE_Y, self.WIDTH, self.TALLNESS = BLOCK_TYPE.value

        self.PERSISTENT = PERSISTENT
        self.vel = DIR.none
        self.alive = True

    # Only call super().update(game) on Solids that can move
    def update(self, game) -> None:
        # Y-movement and gravity
        self.y = min(self.y + self.vel_y, FLOOR_HEIGHT - self.TALLNESS)
        if self.FALLS:
            self.vel_y = self.vel_y + GRAVITY if self.height() > 0 else 0

        self.vel = self.dir()

    def draw(self, game) -> None:
        pyxel.blt(
            self.x - game.x * 8,
            self.y,
            0, # image map that we want to use
            self.SPRITE_X,
            self.SPRITE_Y,
            self.WIDTH,
            self.TALLNESS,
            12 # color, blue, so it becomes transparent
        )

    def height(self) -> float:
        return max(0, FLOOR_HEIGHT - self.TALLNESS - self.y)
    
    def dir(self) -> DIR:
        vel_x = self.vel_x
        vel_y = self.vel_y
        dir = None

        if vel_x > 0:
            if vel_y > 0:
                dir = DIR.down_right
            elif vel_y == 0:
                dir = DIR.right
            else:
                dir = DIR.up_right
        elif vel_x == 0:
            if vel_y > 0:
                dir = DIR.down
            elif vel_y == 0:
                dir = DIR.none
            else:
                dir = DIR.up
        else:
            if vel_y > 0:
                dir = DIR.down_left
            elif vel_y == 0:
                dir = DIR.left
            else:
                dir = DIR.up_left
        
        return dir

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
        return ((self.x, self.y), (self.x + self.WIDTH, self.y), (self.x, self.y + self.TALLNESS), (self.x + self.WIDTH, self.y + self.TALLNESS))


class Block(Solid):
    def update(self, game) -> None:
        super().update(game)
        col = self.collides(game.mario.corners())
        con_1 = col != DIR.none
        con_2 = np.dot(col.value, DIR.up.value) < np.sin(np.pi / 4)
        if con_1 and con_2:
            self.destroy(game)
    
    def destroy(self, game):
        pass #game.solids.list[1].list.remove(self)


class Enemy(Solid):
    pass


class Goomba(Enemy):
    pass


class Pipe(Solid):
    def __init__(self, BLOCK_TYPE, STARTING_X, STARTING_Y, STARTING_VEL_X, STARTING_VEL_Y, HEIGHT=2, FALLS=False, PERSISTENT=False) -> None:
        self.parts = My_Collection(Pipe.Part)
        self.HEIGHT = HEIGHT
        self.parts.new(BLOCK_TYPES.pipe_head, STARTING_X, STARTING_Y, STARTING_VEL_X, STARTING_VEL_Y)
        for i in range(1, int(HEIGHT)):
            self.parts.new(BLOCK_TYPES.pipe_body, STARTING_X, STARTING_Y + 16 * i, STARTING_VEL_X, STARTING_VEL_Y)
        if self.HEIGHT - int(HEIGHT):
            self.parts.new(BLOCK_TYPES.half_pipe_body, STARTING_X, STARTING_Y + 16 * int(HEIGHT), STARTING_VEL_X, STARTING_VEL_Y)

    def update(self, game) -> None:
        self.parts.update(game)
    
    def draw(self, game) -> None:
        self.parts.draw(game)
    
    class Part(Solid):
        pass
        