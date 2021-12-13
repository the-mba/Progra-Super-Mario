import Solid

class Blocks:
    def __init__(self) -> None:
        self.list = []
    
    def draw(self, level_x) -> None:
        for block in self.list:                
            block.draw(level_x)

    def new(self, STARTING_X, STARTING_Y,  STARTING_VEL_X, STARTING_VEL_Y,  WIDTH, TALLNESS,  SPRITE_X, SPRITE_Y, FLOOR_HEIGHT):
        new_block = Block(STARTING_X, STARTING_Y,  STARTING_VEL_X, STARTING_VEL_Y,  WIDTH, TALLNESS,  SPRITE_X, SPRITE_Y, False, FLOOR_HEIGHT)
        self.list.append(new_block)
        return new_block

class Block(Solid.Solid):
    def __init__(self, STARTING_X, STARTING_Y, STARTING_VEL_X, STARTING_VEL_Y, WIDTH, TALLNESS, SPRITE_X, SPRITE_Y, PERSISTENT, FLOOR_HEIGHT) -> None:
        super().__init__(STARTING_X, STARTING_Y, STARTING_VEL_X, STARTING_VEL_Y, WIDTH, TALLNESS, SPRITE_X, SPRITE_Y, PERSISTENT, FLOOR_HEIGHT)