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

class BLOCK_TYPES(enum.Enum):
    pipe = (32, 0, 32, 32)  # just a placeholder, these values shouldn't be directly used. Instead, it should create a pipe_head and several pipe_body
    mario = (0, 48, 16, 16)
    brick = (0, 16, 16, 16)
    question = (16, 0, 16, 16)
    goomba = (32, 48, 16, 16)
    pipe_head = (32, 0, 32, 16)
    pipe_body = (32, 16, 32, 16)