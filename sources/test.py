from Entity import Entity
from Helper import *
from Helper import BLOCK_TYPES as B_T
from Mario import Mario
"""
l = [1, 2, 3, 4, 5]
print(tuple(enumerate(l)))

print(B_T["goomba"].value)

print(eval("STARTING_" + "GOOMBA" + "S"))

print ( map ( print, l) )


def x(a):
    return a*a

for e in map(x, l):
    print(e)
"""

corner = (0, 0)
center = (1, 1)
width = corner[0] - center[0]
tallness = corner[1] - center[1]

vector = [abs(p - c) / measure for (p, c, measure) in zip(corner, center, (width, tallness))]
vector_magnitude = math.sqrt(sum([pow(sub, 2) for sub in vector]))
vector_magnitude_one = tuple([sub / vector_magnitude for sub in vector])

print(f'{DIR.get_DIR_with_similar_coords(vector_magnitude_one) = }')