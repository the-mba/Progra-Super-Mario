from Entity import *
from Helper import *

class My_Collection:
    def __init__(self, *elements) -> None:
        self.list = elements

    def update(self) -> None:
        for element in self.list:
            element.update(self.game)

    def draw(self) -> None:
        for element in self.list:                
            element.draw(self.game)

    def add(self, new_element):
        self.list.append(new_element)