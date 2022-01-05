import math
from enum import Enum, auto

DEBUG = True
OFFSET = -12 if DEBUG else 0

# Background
GAME_WIDTH = 256
GAME_HEIGHT = 192
BACKGROUND_RIGHT_MOVEMENT_THRESHOLD = GAME_WIDTH * 0.6
FLOOR_HEIGHT = GAME_HEIGHT - 32

# Mario's sprite position and size
MARIO_TALLNESS = 16
MARIO_WIDTH = MARIO_TALLNESS
MARIO_SPRITE_X = 0
MARIO_SPRITE_Y = 48

# Mario movement, and derivatives
MARIO_STARTING_X = 140
MARIO_STARTING_Y = FLOOR_HEIGHT - MARIO_TALLNESS  # (192 -32) -16 = 144
MARIO_STARTING_VEL_X = 0
MARIO_STARTING_VEL_Y = 0
MARIO_JUMPING_INITIAL_SPEED = -20
MARIO_ACC_X = 1.5 # acceleration on the x axis (instantaneously applied)

# Universal Constant
GRAVITY = 2
AIR_FRICTION_COEFFICIENT = 0.15

# GUI
POS_POINTS = 0.1
POS_COINS = 0.3
POS_WORLD = 0.6
POS_TIME = 0.8

# STARTING ENTITIES
# -----------------
# EL TILEMAP de altura 84 SE QUEDA EN EL PIXEL de altura 80 !!!

STARTING_BRICKS = [] # (x, y): position
STARTING_QUESTION_BRICKS = [] # (x, y): position
STARTING_CLEAR_BRICKS = [] # (x, y): position
STARTING_GOOMBAS = [
    (42*8,      144 + OFFSET),
    (76 * 8,    144 + OFFSET),
    (106 * 8,   144 + OFFSET),
    (110 * 8,   144 + OFFSET)
] # (x, y, vel_x, vel_y): position and velocity
STARTING_PIPES = [(56*8 + OFFSET,   80 + 3 * 16,    2),
                  (72*8 + OFFSET,   80 + 1 * 16,    4),
                  (96*8 + OFFSET,   80 - 8,       5.5),
                  (120*8 + OFFSET,  80 - 8,       5.5)
] # (x, y, tallness): where tallness can be 0.5, 1, 1.5, etc.
STARTING_DECORS = [] # (x, y): position

class DIR(Enum):
    def angle(self) -> float:
        return math.atan2(self[1], self[0])     
    
    def get_DIR_with_similar_coords(coords):
        for dir in DIR:
            if all([abs(dir[i] - coords[i]) < 10 ^(-6) for i in range(len(dir))]):
                return dir

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


class BLOCK_TYPES(Enum):
    # (x, y, w, h)
    #  x, y:        top-left corner of the sprite
    #        w, h:  width and height of the sprite

    collection = (-1, -1, -1, 1)

    mario = (0, 48, 16, 16)

    mushroom = (0, 32, 16, 16)

    brick = (0, 16, 16, 16)
    clear_brick = (16, 16, 16, 16)
    question_brick = (16, 0, 16, 16)

    goomba = (32, 48, 16, 16)

    pipe = (32, 0, 32, 32)  # just a placeholder, these values shouldn't be directly used. Instead, it should create a pipe_head and several pipe_body
    pipe_head = (32, 0, 32, 16)
    pipe_body = (32, 16, 32, 16)
    pipe_half_body = (32, 16, 32, 8)

    cloud = (16, 64, 3 *16, 1.5 *16)


class EFECTS(auto):
    Super = auto()
    Cow = auto()

# TODO:
# Collisions