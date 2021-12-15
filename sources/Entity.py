import pyxel, math
import numpy as np

from Helper import *
from My_Collection import My_Collection

class Entity:
    def __init__(self, BLOCK_TYPE, STARTING_X, STARTING_Y, STARTING_VEL_X, STARTING_VEL_Y, HEIGHT=1, FALLS=False, PERSISTENT=False) -> None:
        self.BLOCK_TYPE = BLOCK_TYPE
        self.FALLS = FALLS
        
        self.x = STARTING_X
        self.y = STARTING_Y

        self.prev_x = self.x
        self.prev_y = self.y
        

        self.vel_x = STARTING_VEL_X
        self.vel_y = STARTING_VEL_Y

        self.SPRITE_X, self.SPRITE_Y, self.WIDTH, self.TALLNESS = BLOCK_TYPE.value

        self.PERSISTENT = PERSISTENT
        self.alive = True

    # Only call super().update(game) on Solids that can move
    def update(self, game) -> None:
        self.prev_y = self.y
        # Y-movement and gravity
        self.y = min(self.y + self.vel_y, FLOOR_HEIGHT - self.TALLNESS)
        if self.FALLS and self.height():
            self.vel_y += GRAVITY
        else:
            self.vel_y = 0

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
    
    """ def dir(self) -> DIR:
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
        
        return dir """

    def collides(self, corners) -> tuple:
        col, side = False, DIR.none

        if ((self.x <= corners[0][0] and corners[0][0] <= self.x + self.WIDTH) and 
            (self.y <= corners[0][1] and corners[0][1] <= self.y + self.TALLNESS)):
            side = DIR.up_left
            col = True

        if ((self.x <= corners[1][0] and corners[1][0] <= self.x + self.WIDTH) and
            (self.y <= corners[1][1] and corners[1][1] <= self.y + self.TALLNESS)):
            side = DIR.up_right
            col = True

        if ((self.x <= corners[2][0] and corners[2][0] <= self.x + self.WIDTH) and
            (self.y <= corners[2][1] and corners[2][1] <= self.y + self.TALLNESS)):
            side = DIR.down_left
            col = True

        if ((self.x <= corners[3][0] and corners[3][0] <= self.x + self.WIDTH) and
            (self.y <= corners[3][1] and corners[3][1] <= self.y + self.TALLNESS)):
            side = DIR.down_right 
            col = True

        return col, side         
        
    def corners(self) -> tuple:
        return ((self.x, self.y), (self.x + self.WIDTH, self.y), (self.x, self.y + self.TALLNESS), (self.x + self.WIDTH, self.y + self.TALLNESS))


class Block(Entity):
    def update(self, game) -> None:
        super().update(game)
        col, side = self.collides(game.mario.corners())
        if col:
            print("COLLISION DETECTED!!!")
        else:
            print("Not anymore")

        """col_dir = self.collides(game.mario.corners())
        con_1 = col_dir != DIR.none
        if con_1:
            print(col_dir.value, DIR.up.value, np.dot(col_dir.value, DIR.up.value))
        con_2 = np.dot(col_dir.value, DIR.up.value) > np.cos(math.radians(45))
        if con_1 and con_2:
            self.destroy(game)"""  # THIS WHOLE THING IS KINDA BS, NEEDS A REWRITE !!!
    
    def destroy(self, game):
        game.solids.list[1].list.remove(self)
        game.mario.prev_y = game.mario.y
        game.mario.y = self.y + self.TALLNESS
        game.mario.vel_y = 0


class Enemy(Entity):
    pass


class Goomba(Enemy):
    pass


class Pipe(Entity):
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
    
    class Part(Entity):
        pass

class Decor(Entity):
    pass

class Mushroom(Entity):
    def update(self, game) -> None:
        super().update(game)

        col, side = self.collides(game.mario.corners())
        if col:
            print("COLLISION DETECTED!!!")
        con_1 = side != DIR.none
        if con_1:
            print(side.value, DIR.up.value, np.dot(side.value, DIR.up.value))
        con_2 = True
        if con_1 and con_2:
            pass
        pyxel.quit()
        print("EEEEEEEEEE" * 10000)