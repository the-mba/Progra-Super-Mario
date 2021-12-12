import pyxel

class GUI:
    def __init__(self, DEBUG, WIDTH, BACKGROUND_RIGHT_MOVEMENT_THRESHOLD) -> None:
        self.background = GUI.Background(WIDTH, BACKGROUND_RIGHT_MOVEMENT_THRESHOLD)
        self.DEBUG = DEBUG
    
    def update(self, mario_x):
        self.background.update(mario_x)
        
    def draw(self):
        self.background.draw()

        #draw coin
        pyxel.blt(40, 4, 0, 48, 104, 8, 8, 7)

        # draw texts
        name_str = "MARIO"
        pyxel.text(5, 4, name_str, 1)
        pyxel.text(4, 4, name_str, 7)
        if self.DEBUG: self.mario.coins = 0
        points_str = f'{self.mario.coins:06d}'
        pyxel.text(5, 10, points_str, 1)
        pyxel.text(4, 10, points_str, 7)
        if self.DEBUG: self.mario.coins = 0
        coins_str = 'x' + f'{self.mario.coins:02d}'
        pyxel.text(50, 6, coins_str, 1)
        pyxel.text(51, 6, coins_str, 7)
        world_str = "WORLD"
        pyxel.text(70, 4, world_str, 1)
        pyxel.text(71, 4, world_str, 7)
        world_name = "1 - 1"
        pyxel.text(70, 10, world_name, 1)
        pyxel.text(71, 10, world_name, 7)
        time_name = "TIME"
        pyxel.text(110, 4, time_name, 1)
        pyxel.text(111, 4, time_name, 7)
        if self.DEBUG: self.mario.time = 0
        time_name = f'{self.mario.time:02d}'
        pyxel.text(110, 10, time_name, 1)
        pyxel.text(111, 10, time_name, 7)
    
    class Background:
        def __init__(self, WIDTH, BACKGROUND_RIGHT_MOVEMENT_THRESHOLD) -> None:
            self.background = pyxel.tilemap(0)
            self.game_width = WIDTH
            self.right_movement_threshold = BACKGROUND_RIGHT_MOVEMENT_THRESHOLD

            self.x = 0
        
        def update(self, mario_x) -> float:
            if mario_x > self.right_movement_threshold:
                self.x += 1/4
                new_mario_x = self.right_movement_threshold
            else:
                new_mario_x = mario_x
            return new_mario_x
        
        def draw(self):
            # draw light blue background
            pyxel.cls(12)

            print("""qidbqjdewdefewfdewfewfeqidbqjdewdefewfdewfewfeqidbqjdewdefewfdewfewfeqidbqjdewdefewfdewfewfeqidbqjdewdefewfdewfewfeqidbqjdewdefewfdewfewfeqidbqjdewdefewfdewfewfeqidbqjdewdefewfdewfewfeqidbqjdewdefewfdewfewfeqidbqjdewdefewfdewfewfeqidbqjdewdefewfdewfewfeqidbqjdewdefewfdewfewfeqidbqjdewdefewfdewfewfeqidbqjdewdefewfdewfewfeqidbqjdewdefewfdewfewfeqidbqjdewdefewfdewfewfeqidbqjdewdefewfdewfewfeqidbqjdewdefewfdewfewfeqidbqjdewdefewfdewfewfeqidbqjdewdefewfdewfewfeqidbqjdewdefewfdewfewfeqidbqjdewdefewfdewfewfeqidbqjdewdefewfdewfewfeqidbqjdewdefewfdewfewfeqidbqjdewdefewfdewfewfeqidbqjdewdefewfdewfewfeqidbqjdewdefewfdewfewfeqidbqjdewdefewfdewfewfeqidbqjdewdefewfdewfewfeqidbqjdewdefewfdewfewfeqidbqjdewdefewfdewfewfeqidbqjdewdefewfdewfewfeqidbqjdewdefewfdewfewfeqidbqjdewdefewfdewfewfeqidbqjdewdefewfdewfewfeqidbqjdewdefewfdewfewfeqidbqjdewdefewfdewfewfeqidbqjdewdefewfdewfewfeqidbqjdewdefewfdewfewfeqidbqjdewdefewfdewfewfeqidbqjdewdefewfdewfewfeqidbqjdewdefewfdewfewfeqidbqjdewdefewfdewfewfeqidbqjdewdefewfdewfewfeqidbqjdewdefewfdewfewfeqidbqjdewdefewfdewfewfeqidbqjdewdefewfdewfewfeqidbqjdewdefewfdewfewfeqidbqjdewdefewfdewfewfeqidbqjdewdefewfdewfewfeqidbqjdewdefewfdewfewfeqidbqjdewdefewfdewfewfeqidbqjdewdefewfdewfewfeqidbqjdewdefewfdewfewfeqidbqjdewdefewfdewfewfeqidbqjdewdefewfdewfewfeqidbqjdewdefewfdewfewfeqidbqjdewdefewfdewfewfeqidbqjdewdefewfdewfewfeqidbqjdewdefewfdewfewfeqidbqjdewdefewfdewfewfeqidbqjdewdefewfdewfewfeqidbqjdewdefewfdewfewfeqidbqjdewdefewfdewfewfeqidbqjdewdefewfdewfewfeqidbqjdewdefewfdewfewfeqidbqjdewdefewfdewfewfeqidbqjdewdefewfdewfewfe""")

            # draw tilemap
            pyxel.bltm(0, 50, 0, self.x, 88, 160, 32)
