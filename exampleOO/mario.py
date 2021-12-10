class Mario:
    """ This class stores all the information needed for Mario"""
    def __init__(self, x: int, y: int, dir: bool):
        """ This method creates the Mario object
        @param x the starting x of Mario
        @param y the starting y of Mario
        @param dir a boolean to store the initial direction of Mario.
                True is facing right, False is facing left"""
        self.x = x
        self.y = y
        self.direction = dir
        # Here we are assuming Mario will be always placed at the first
        # bank at first position and it will have a 16x16 size
        self.sprite = (0, 0, 0, 16, 16)
        # We also assume that Mario will always have three lives in the beginning
        self.lives = 3

    def move(self, direction: str, size: int):
        """ This is an example of a method that moves Mario, it receives the
        direction and the size of the board"""
        # Checking the current horizontal size of Mario to stop him before
        # he reaches the right border
        mario_x_size = self.sprite[3]
        if direction.lower() == 'right' and self.x < size - mario_x_size:
            self.x = self.x + 1
        elif direction.lower() == 'left' and self.x > 0:
            # I am assuming that if it is not right it will be left
            self.x -= 1