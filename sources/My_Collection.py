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

    def new(self, BLOCK_TYPE, STARTING_X, STARTING_Y,  STARTING_VEL_X, STARTING_VEL_Y, FLOOR_HEIGHT, HEIGHT=1, PERSISTENT=False):
        new_element = self.element_type(BLOCK_TYPE, STARTING_X, STARTING_Y,  STARTING_VEL_X, STARTING_VEL_Y, FLOOR_HEIGHT, HEIGHT, PERSISTENT)
        self.list.append(new_element)
        return new_element


class My_Meta_Collection(My_Collection):
    def __init__(self, *types) -> None:
        self.list = []
        for t in types:
            self.list.append(My_Collection(t))

    def new(self, BLOCK_TYPE, STARTING_X, STARTING_Y,  STARTING_VEL_X, STARTING_VEL_Y, FLOOR_HEIGHT, HEIGHT=1, PERSISTENT=False):
        pass