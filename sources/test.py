from Entity import Entity
from Helper import *
from Helper import BLOCK_TYPES as B_T

def collides(self, corners) -> DIR:
        side = DIR.none

        if ((self.x <= corners[0][0] and corners[0][0] <= self.x + self.WIDTH) and 
            (self.y <= corners[0][1] and corners[0][1] <= self.y + self.TALLNESS)):
            side = DIR.up_left

        if ((self.x <= corners[1][0] and corners[1][0] <= self.x + self.WIDTH) and
            (self.y <= corners[1][1] and corners[1][1] <= self.y + self.TALLNESS)):
            side = DIR.up_right

        if ((self.x <= corners[2][0] and corners[2][0] <= self.x + self.WIDTH) and
            (self.y <= corners[2][1] and corners[2][1] <= self.y + self.TALLNESS)):
            side = DIR.down_left

        if ((self.x <= corners[3][0] and corners[3][0] <= self.x + self.WIDTH) and
            (self.y <= corners[3][1] and corners[3][1] <= self.y + self.TALLNESS)):
            side = DIR.down_right 

        return side    

E = Entity(B_T.goomba, 42 * 8, 144, 0, 0)
F = Entity(B_T.goomba, 42 * 8 - OFFSET, 144 + OFFSET, 0, 0)

print(  )#####DEPRECATED: collides( F.corners() )  )


""" MARIO_AIR_FRICTION = -1
vel_x_prev = -5555.0
vel_x_post = ( abs(vel_x_prev) + MARIO_AIR_FRICTION ) * abs(vel_x_prev) / vel_x_prev if vel_x_prev != 0 else 0
print(vel_x_post)
TESTED AND OK!!  """