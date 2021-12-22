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
    
    def draw(self, game) -> None:
        for element in self.list:                
            element.draw(game)

    def new(self, BLOCK_TYPE, STARTING_X, STARTING_Y,  STARTING_VEL_X=0, STARTING_VEL_Y=0, HEIGHT=1, PERSISTENT=False):
        new_element = self.element_type(BLOCK_TYPE, STARTING_X, STARTING_Y,  STARTING_VEL_X, STARTING_VEL_Y, HEIGHT, PERSISTENT)
        self.list.append(new_element)
        return new_element
    
    def news(self, BLOCK_TYPE, POS, VEL=[]):
        for i, element in enumerate(POS):
            new_element = self.element_type(
                BLOCK_TYPE,
                element[0], element[1],
                VEL[i][0] if VEL != [] else 0,
                VEL[i][1] if VEL != [] else 0)
            self.list.append(new_element)

