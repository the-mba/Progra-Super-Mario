import math, enum

class DIR(enum.Enum):
    r = math.sqrt(2) / 2
    up = (0, -1)
    up_right = (r, -r)
    right = (1, 0)
    down_right = (r, r)
    down = (0, 1)
    down_left = (-r, r)
    left = (-1, 0)
    up_left = (-r, -r)
    none = (0, 0)