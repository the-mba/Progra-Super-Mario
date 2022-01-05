import pyxel, Mario
from Entity import *

class Game:
    def __init__(self) -> None:

        # INIT
        game = self
        game.x = 0

        # ENTITIES
        game.bricks = [Brick(game, *e) for e in STARTING_BRICKS]
        game.question_bricks = [Question_Brick(game, *e) for e in STARTING_QUESTION_BRICKS]
        game.clear_bricks = [Clear_Brick(game, *e) for e in STARTING_CLEAR_BRICKS]
        game.goombas = [Goomba(game, *e) for e in STARTING_GOOMBAS]
        game.pipes = [Pipe(game, *e) for e in STARTING_PIPES]
        game.decors = [Cloud(game, *e) for e in STARTING_DECORS]

        game.solids = [game.bricks, game.question_bricks, game.clear_bricks, game.goombas, game.pipes, game.decors]

        game.mario = Mario.Mario(game)

        # PYXEL
        pyxel.init(GAME_WIDTH, GAME_HEIGHT, caption="New Super Mario Bros.")
        pyxel.load("../assets/marioassets.pyxres")
        pyxel.run(game.update, game.draw)

    def update(self) -> None:
        game = self

        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        
        [solid.update() for sublist in game.solids for solid in sublist]

        [solid.update() for sublist in game.solids for solid in sublist]

        # update mario returns the extra x to move_right
        game.x += game.mario.update()

    def draw(self) -> None:
        game = self

        game.draw_background_and_gui()

        [solid.draw() for sublist in game.solids for solid in sublist]

        game.mario.draw()
    
    def draw_background_and_gui(self) -> None:
        game = self

        # draw light blue background
        pyxel.cls(12)
        # draw tilemap
        pyxel.bltm(- (game.x % 8), 0, 0, game.x // 8, 74, 128, 128)
        # pyxel.bltm(0, 0, 0, game.x % 256 - 256, 74, 128, 128) # TODO: remove this and convert all coordinates to modulo 256 so that the whole game can infinitely repeat to the right

        #draw coin
        pyxel.blt(GAME_WIDTH * POS_COINS - 8 - 2, 4, 0, 48, 104, 8, 8, 7) # -8 is the coind GAME_WIDTH, -2 is some spacing

        # draw texts
        name_str = "MARIO"
        pyxel.text(GAME_WIDTH * POS_POINTS, 4, name_str, 1)
        pyxel.text(GAME_WIDTH * POS_POINTS + 1, 4, name_str, 7)
        if DEBUG: game.points = 0
        points_str = f'{game.points:06d}'
        pyxel.text(GAME_WIDTH * POS_POINTS, 10, points_str, 1)
        pyxel.text(GAME_WIDTH * POS_POINTS + 1, 10, points_str, 7)
        if DEBUG: mario_coins = 0
        coins_str = 'x' + f'{mario_coins:02d}'
        pyxel.text(GAME_WIDTH * POS_COINS, 6, coins_str, 1)
        pyxel.text(GAME_WIDTH * POS_COINS + 1, 6, coins_str, 7)
        world_str = "WORLD"
        pyxel.text(GAME_WIDTH * POS_WORLD + 1, 4, world_str, 1)
        pyxel.text(GAME_WIDTH * POS_WORLD, 4, world_str, 7)
        world_name = "1 - 1"
        pyxel.text(GAME_WIDTH * POS_WORLD, 10, world_name, 1)
        pyxel.text(GAME_WIDTH * POS_WORLD + 1, 10, world_name, 7)
        time_name = "TIME"
        pyxel.text(GAME_WIDTH * POS_TIME, 4, time_name, 1)
        pyxel.text(GAME_WIDTH * POS_TIME + 1, 4, time_name, 7)
        if DEBUG: mario_time = 0
        time_name = f'{mario_time:02d}'
        pyxel.text(GAME_WIDTH * POS_TIME, 10, time_name, 1)
        pyxel.text(GAME_WIDTH * POS_TIME + 1, 10, time_name, 7)

        if DEBUG:
            pyxel.text(GAME_WIDTH * 0.6, 80, str(game.mario.x), 1)
            pyxel.text(GAME_WIDTH * 0.6, 86, str(game.mario.vel_x), 1)