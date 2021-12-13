import Solid

s= """
class Blocks:
    def __init__(self) -> None:
        self.list = []
    
    def draw(self, level_x) -> None:
        for block in self.list:                
            block.draw(level_x)

    def new(self, BLOCK_TYPE, STARTING_X, STARTING_Y,  STARTING_VEL_X, STARTING_VEL_Y,  WIDTH, TALLNESS, FLOOR_HEIGHT):
        new_block = Block(BLOCK_TYPE, STARTING_X, STARTING_Y,  STARTING_VEL_X, STARTING_VEL_Y,  WIDTH, TALLNESS, False, FLOOR_HEIGHT)
        self.list.append(new_block)
        return new_block
"""


class Block(Solid.Solid):
    def __init__(self, BLOCK_TYPE, STARTING_X, STARTING_Y, STARTING_VEL_X, STARTING_VEL_Y, WIDTH, TALLNESS, PERSISTENT, FLOOR_HEIGHT) -> None:
        super().__init__(STARTING_X, STARTING_Y, STARTING_VEL_X, STARTING_VEL_Y, WIDTH, TALLNESS, *BLOCK_TYPE.value, PERSISTENT, FLOOR_HEIGHT)
        self.BLOCK_TYPE = BLOCK_TYPE
    