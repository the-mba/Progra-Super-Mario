from Entity import Entity
from Helper import *
from Helper import BLOCK_TYPES as B_T

l = [1, 2, 3, 4, 5]
print(tuple(enumerate(l)))

print(B_T["goomba"].value)

print(eval("STARTING_" + "GOOMBA" + "S"))

print ( map ( print, l) )


def x(a):
    return a*a

for e in map(x, l):
    print(e)