import pyxel
from Helper import *

class My_Collection:
    def __init__(self, *element_types) -> None:
        self.list = []
        if len(element_types) == 1:
            self.element_type = element_types[0]
        else:
            for element_type in element_types:
                self.list.append(self.__class__(element_type))
    
    def update(self, game) -> None:
        for element in self.list:
            element.update(game)
    
    def draw(self, level_x) -> None:
        for element in self.list:                
            element.draw(level_x)

    def new(self, BLOCK_TYPE, STARTING_X, STARTING_Y,  STARTING_VEL_X, STARTING_VEL_Y, FLOOR_HEIGHT, HEIGHT=1, PERSISTENT=False):
        if self.element_type == type(self):
            for block_type in BLOCK_TYPE:
                self.list.append(self.__class__(block_type))
        else:
            new_element = self.element_type(BLOCK_TYPE, STARTING_X, STARTING_Y,  STARTING_VEL_X, STARTING_VEL_Y, FLOOR_HEIGHT, HEIGHT, PERSISTENT)
            self.list.append(new_element)
            return new_element