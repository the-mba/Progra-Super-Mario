import pyxel

class My_Collection:
    def __init__(self, element_type) -> None:
        self.list = []
        self.element_type = element_type
    
    def update(self, mario) -> None:
        for element in self.list:
            element.update(mario)
    
    def draw(self, level_x) -> None:
        for element in self.list:                
            element.draw(level_x)

    def new(self, BLOCK_TYPE, STARTING_X, STARTING_Y,  STARTING_VEL_X, STARTING_VEL_Y,  WIDTH, TALLNESS, PERSISTENT, FLOOR_HEIGHT):
        new_block = self.element_type(BLOCK_TYPE, STARTING_X, STARTING_Y,  STARTING_VEL_X, STARTING_VEL_Y,  WIDTH, TALLNESS, PERSISTENT, FLOOR_HEIGHT)
        self.list.append(new_block)
        return new_block