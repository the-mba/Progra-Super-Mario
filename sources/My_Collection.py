import pyxel
from Helper import *

class My_Collection:
    def __init__(self, *element_types) -> None:
        self.list = []
        if len(element_types) == 1:
            print(element_types)
            self.element_type = element_types[0]
            if self.element_type.__name__ != "Part":
                self.news(eval("STARTING_" + self.element_type.__name__.upper() + "S"))
        else:
            for element in element_types:
                if element.__class__ == self.__class__:
                    self.list.append(element)
                else:
                    self.list.append(self.__class__(element))
    
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
    
    def news(self, PARAMETERS):
        for i, element in enumerate(PARAMETERS):
            if self.element_type.__name__ == "Pipe":
                self.new(
                    BLOCK_TYPES[self.element_type.__name__.lower()],
                    element[0], element[1], 0, 0, element[2]
                )
            else:
                self.new(
                    BLOCK_TYPES[self.element_type.__name__.lower()],
                    element[0], element[1],
                    element[2] if len(element) > 2 else 0,
                    element[3] if len(element) > 3 else 0)

