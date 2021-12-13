import pyxel

POS_POINTS = 0.1
POS_COINS = 0.3
POS_WORLD = 0.6
POS_TIME = 0.8

class GUI:
    def __init__(self, DEBUG, WIDTH, BACKGROUND_RIGHT_MOVEMENT_THRESHOLD, BACKGROUND_SPEED) -> None:
        self.background = GUI.Background(BACKGROUND_RIGHT_MOVEMENT_THRESHOLD, BACKGROUND_SPEED)
        self.DEBUG = DEBUG
        self.WIDTH = WIDTH
    
    def update(self) -> None:
        self.background.update()
        
    def draw(self, tilemap_x, mario_points, mario_coins, mario_time) -> None:
        self.background.draw(tilemap_x)

        #draw coin
        pyxel.blt(self.WIDTH * POS_COINS - 8 - 2, 4, 0, 48, 104, 8, 8, 7) # -8 is the coind width, -2 is some spacing

        # draw texts
        name_str = "MARIO"
        pyxel.text(self.WIDTH * POS_POINTS, 4, name_str, 1)
        pyxel.text(self.WIDTH * POS_POINTS + 1, 4, name_str, 7)
        if self.DEBUG: mario_points = 0
        points_str = f'{mario_points:06d}'
        pyxel.text(self.WIDTH * POS_POINTS, 10, points_str, 1)
        pyxel.text(self.WIDTH * POS_POINTS + 1, 10, points_str, 7)
        if self.DEBUG: mario_coins = 0
        coins_str = 'x' + f'{mario_coins:02d}'
        pyxel.text(self.WIDTH * POS_COINS, 6, coins_str, 1)
        pyxel.text(self.WIDTH * POS_COINS + 1, 6, coins_str, 7)
        world_str = "WORLD"
        pyxel.text(self.WIDTH * POS_WORLD + 1, 4, world_str, 1)
        pyxel.text(self.WIDTH * POS_WORLD, 4, world_str, 7)
        world_name = "1 - 1"
        pyxel.text(self.WIDTH * POS_WORLD, 10, world_name, 1)
        pyxel.text(self.WIDTH * POS_WORLD + 1, 10, world_name, 7)
        time_name = "TIME"
        pyxel.text(self.WIDTH * POS_TIME, 4, time_name, 1)
        pyxel.text(self.WIDTH * POS_TIME + 1, 4, time_name, 7)
        if self.DEBUG: mario_time = 0
        time_name = f'{mario_time:02d}'
        pyxel.text(self.WIDTH * POS_TIME, 10, time_name, 1)
        pyxel.text(self.WIDTH * POS_TIME + 1, 10, time_name, 7)
    
    class Background: #+ 16 * 8
        def __init__(self, BACKGROUND_RIGHT_MOVEMENT_THRESHOLD, BACKGROUND_SPEED) -> None:
            self.BACKGROUND_RIGHT_MOVEMENT_THRESHOLD = BACKGROUND_RIGHT_MOVEMENT_THRESHOLD
            self.BACKGROUND_SPEED = BACKGROUND_SPEED
        
        def update(self) -> None:
            pass

        def draw(self, tilemap_x) -> None:
            # draw light blue background
            pyxel.cls(12)

            # draw tilemap
            pyxel.bltm(0, 0, 0, tilemap_x % 256, 74, 128, 128)

            pyxel.bltm(0, 0, 0, tilemap_x % 256 - 256, 74, 128, 128)
