import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTIONS
from code.Level import Level
from code.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=[WIN_WIDTH, WIN_HEIGHT])
        pygame.display.set_caption('RoadRush')

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()


            if menu_return == MENU_OPTIONS[0]:
                level = Level(self.window, "Level1")
                level.run()
            if menu_return == MENU_OPTIONS[1]:
                pass
            elif menu_return == MENU_OPTIONS[2]:
                pygame.quit()  # CLOSE THE WINDOW
                quit()
            else:
                pass