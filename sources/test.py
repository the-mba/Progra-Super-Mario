from Entity import Entity
from Helper import *
from Helper import BLOCK_TYPES as B_T

def collides(self, corners) -> DIR:
    qprint(  "")#####DEPRECATED: collides( F.corners() )  )


""" MARIO_AIR_FRICTION = -1
vel_x_prev = -5555.0
vel_x_post = ( abs(vel_x_prev) + MARIO_AIR_FRICTION ) * abs(vel_x_prev) / vel_x_prev if vel_x_prev != 0 else 0
print(vel_x_post)
TESTED AND OK!!  """

l = [1, 2, 3, 4, 5]
print(tuple(enumerate(l)))

print(B_T["goomba"].value)

print(eval("STARTING_" + "GOOMBA" + "S"))

print ( map ( print, l) )


def x(a):
    return a*a

for e in map(x, l):
    print(e)