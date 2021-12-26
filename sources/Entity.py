import pyxel, math
import numpy as np

from Helper import *
from My_Collection import My_Collection

class Entity:
    def __init__(self, BLOCK_TYPE, STARTING_X, STARTING_Y, STARTING_VEL_X=0, STARTING_VEL_Y=0, HEIGHT=1, FALLS=False, PERSISTENT=False) -> None:
        self.BLOCK_TYPE = BLOCK_TYPE
        self.FALLS = FALLS
        
        self._x = STARTING_X
        self._y = STARTING_Y

        self._x_prev = self.x
        self._y_prev = self.y
        

        self.vel_x = STARTING_VEL_X
        self.vel_y = STARTING_VEL_Y

        self.SPRITE_X, self.SPRITE_Y, self.WIDTH, self.TALLNESS = BLOCK_TYPE.value

        self.PERSISTENT = PERSISTENT
        self.alive = True
    
    @property
    def x(self):
        return self._x
    @x.setter
    def x(self, value):
        self._x_prev = self._x
        self._x = value
    
    @property
    def y(self):
        return self._y
    @y.setter
    def y(self, value):
        self._y_prev = self._y
        self._y = min(value, FLOOR_HEIGHT - self.TALLNESS)

    # Only call super().update(game) on Entities that can move
    def update(self, game) -> None:
        # X-movement
        self.x += self.vel_x
        # Y-movement and gravity
        self.y += self.vel_y
        if self.FALLS and self.height():
            self.vel_y += GRAVITY
        else:
            self.vel_y = 0
        
        self.vel_x = 0
        """# X-AXIS air friction, so velocity reduces naturally
        if self.vel_x != 0:
            vel_x_prev_abs = abs( self.vel_x )
            vel_x_post_abs = vel_x_prev_abs + MARIO_AIR_FRICTION

            if vel_x_post_abs > 0:
                self.vel_x = (vel_x_post_abs) * abs(self.vel_x) / self.vel_x
            else:
                self.vel_x = 0"""
    
    def draw(self, game) -> None:
        pyxel.blt(
            self.x - game.x,
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
    
    def angle(self) -> float:
        return math.atan2(self.vel_y, self.vel_x)      
        
    def corners(self) -> tuple:
        return ((self.x, self.y), (self.x + self.WIDTH, self.y), (self.x, self.y + self.TALLNESS), (self.x + self.WIDTH, self.y + self.TALLNESS))
    
    def rect_func(self, x) -> float:
        p = (self.y - self._y_prev) / (self.x - self._x_prev)
        return self._y_prev + p * (x - self._x_prev)
    
    def rect_func_inv(self, y) -> float:
        p = (self.x - self._x_prev) / (self.y - self._y_prev)
        return self._x_prev + p * (y - self._y_prev)


class Block(Entity):
    def update(self, game) -> None:
        corners = game.mario.corners()
        side = DIR.none
        a = game.mario.angle()
        #print("Mario's angle is: ", a)
        if ((self.x <= corners[0][0] and corners[0][0] <= self.x + self.WIDTH) and 
            (self.y <= corners[0][1] and corners[0][1] <= self.y + self.TALLNESS)):
            if abs(a - math.radians(90)) < 10 ^(-3):
                side = DIR.down
            elif abs(a - math.radians(180)) < 10 ^(-3):
                side = DIR.right
            else:
                p = game.mario.rect_func(self.x)
                p_inv = game.mario.rect_func_inv(self.y)
                if self.y <= p and p <= self.y + self.TALLNESS:
                    side = DIR.right
                elif self.x <= p_inv and p_inv <= self.x + self.WIDTH:
                    side = DIR.down
                elif math.radians(135) <= a and a <= math.radians(180):
                    side = DIR.right
                else:
                    side = DIR.down

        if ((self.x <= corners[1][0] and corners[1][0] <= self.x + self.WIDTH) and
            (self.y <= corners[1][1] and corners[1][1] <= self.y + self.TALLNESS)):
            if abs(a - math.radians(0)) < 10 ^(-3):
                side = DIR.left
            elif abs(a - math.radians(90)) < 10 ^(-3):
                side = DIR.down
            else:
                p = game.mario.rect_func(self.x - game.mario.WIDTH)
                p_inv = game.mario.rect_func_inv(self.y) + game.mario.WIDTH
                if self.y <= p and p <= self.y + self.TALLNESS:
                    side = DIR.left
                if self.x <= p_inv and p_inv <= self.x + self.WIDTH:
                    side = DIR.down
                elif 0 <= a and a <= math.radians(45):
                    side = DIR.left
                else:
                    side = DIR.down

        if ((self.x <= corners[2][0] and corners[2][0] <= self.x + self.WIDTH) and
            (self.y <= corners[2][1] and corners[2][1] <= self.y + self.TALLNESS)):
            if abs(a - math.radians(180)) < 10 ^(-3):
                side = DIR.right
            elif abs(a - math.radians(-90)) < 10 ^(-3):
                side = DIR.up
            else:
                p = game.mario.rect_func(self.x) + game.mario.TALLNESS
                p_inv = game.mario.rect_func_inv(self.y - game.mario.TALLNESS)
                if self.y <= p and p <= self.y + self.TALLNESS:
                    side = DIR.right
                if self.x <= p_inv and p_inv <= self.x + self.WIDTH:
                    side = DIR.up
                elif math.radians(-180) <= a and a <= math.radians(-135):
                    side = DIR.right
                else:
                    side = DIR.up

        if ((self.x <= corners[3][0] and corners[3][0] <= self.x + self.WIDTH) and
            (self.y <= corners[3][1] and corners[3][1] <= self.y + self.TALLNESS)):
            if abs(a - math.radians(0)) < 10 ^(-3):
                side = DIR.left
            elif abs(a - math.radians(-90)) < 10 ^(-3):
                side = DIR.up
            else:
                p = game.mario.rect_func(self.x - game.mario.WIDTH) + game.mario.TALLNESS
                p_inv = game.mario.rect_func_inv(self.y - game.mario.TALLNESS) + game.mario.WIDTH
                if self.y <= p and p <= self.y + self.TALLNESS:
                    side = DIR.left
                if self.x <= p_inv and p_inv <= self.x + self.WIDTH:
                    side = DIR.up
                elif math.radians(-180) <= a and a <= math.radians(-135):
                    side = DIR.left
                else:
                    side = DIR.up
                    
        if side != DIR.none:
            print("COLLISION DETECTED!!! from", side.name)
        else:
            pass #print("Not anymore")

        """col_dir = self.collides(game.mario.corners())
        con_1 = col_dir != DIR.none
        if con_1:
            print(col_dir.value, DIR.up.value, np.dot(col_dir.value, DIR.up.value))
        con_2 = np.dot(col_dir.value, DIR.up.value) > np.cos(math.radians(45))
        if con_1 and con_2:
            self.destroy(game)"""  # THIS WHOLE THING IS KINDA BS, NEEDS A REWRITE !!!
        
        super().update(game)

    def destroy(self, game):
        game.solids.list[1].list.remove(self)
        game.mario.prev_y = game.mario.y
        game.mario.y = self.y + self.TALLNESS
        game.mario.vel_y = 0


class Brick(Block):
    pass


class Question_Brick(Block):
    pass

class Clear_Brick(Block):
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


class Enemy(Entity):
    pass


class Goomba(Enemy):
    pass

class Mushroom(Entity):
    def update(self, game) -> None:

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











        s = """ def dir(self) -> DIR:
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

        super().update(game)
    
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