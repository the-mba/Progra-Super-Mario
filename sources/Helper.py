import math, enum

DEBUG = 1

GAME_WIDTH = 256
GAME_HEIGHT = 192
BACKGROUND_RIGHT_MOVEMENT_THRESHOLD = GAME_WIDTH * 0.6
BACKGROUND_SPEED = 1
FLOOR_HEIGHT = GAME_HEIGHT - 32

OFFSET = -12 if DEBUG else 0

MARIO_TALLNESS = 16
MARIO_WIDTH = MARIO_TALLNESS
MARIO_SPRITE_X = 0
MARIO_SPRITE_Y = 48

MARIO_STARTING_X = 160
MARIO_STARTING_Y = FLOOR_HEIGHT - MARIO_TALLNESS
MARIO_STARTING_VEL_Y = 0
MARIO_CONSTANT_VEL_X = 3
GRAVITY = 0.5
JUMPING_COEFFICIENT = 1.8

POS_POINTS = 0.1
POS_COINS = 0.3
POS_WORLD = 0.6
POS_TIME = 0.8


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
    none = (0, 0) # only so the dot product is huge and it doesn't compute as a valid movement

class BLOCK_TYPES(enum.Enum):
    collection = (-1, -1, -1, 1)
    mario = (0, 48, 16, 16)
    brick = (0, 16, 16, 16)
    question = (16, 0, 16, 16)
    goomba = (32, 48, 16, 16)
    pipe = (32, 0, 32, 32)  # just a placeholder, these values shouldn't be directly used. Instead, it should create a pipe_head and several pipe_body
    pipe_head = (32, 0, 32, 16)
    pipe_body = (32, 16, 32, 16)
    half_pipe_body = (32, 16, 32, 8)