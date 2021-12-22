import pyxel
from Helper import *

class My_Collection:
    def __init__(self, *element_types) -> None:
        self.list = []
        if len(element_types) == 1:
            self.element_type = element_types[0]
            self.news(exec("STARTING_" + self.element_type.__name__.upper() + "S"))
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
    
    def news(self, POS_AND_OR_VEL):
        for i, element in enumerate(POS_AND_OR_VEL):
            self.new(
                BLOCK_TYPES[self.element_type.__name__.lower()],
                element[0], element[1],
                element[2] if len(element) > 2 else 0,
                element[3] if len(element) > 3 else 0)

