import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, C_BLUE, C_WHITE, MENU_OPTIONS, C_LILAC


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./assets/MenuBg.png')
        self.rect = self.surf.get_rect()

    def run(self):
        selected_option = 0
        pygame.mixer_music.load("./assets/race.mp3")
        pygame.mixer_music.play(-1)

        while True:
            self.window.blit(self.surf, self.rect)
            self.menu_text(60, "RoadRush", C_BLUE, (WIN_WIDTH / 2, 120))
            for i, option in enumerate(MENU_OPTIONS):
                if i == selected_option:
                    self.menu_text(30, option["text"], C_LILAC, (WIN_WIDTH / 2, option["pos"]))
                else:
                    self.menu_text(30, option["text"], C_WHITE, (WIN_WIDTH / 2, option["pos"]))
            pygame.display.flip()


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit() # CLOSE THE WINDOW
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN: # ARROW DOWN
                        if selected_option < len(MENU_OPTIONS) - 1:
                            selected_option += 1
                    if event.key == pygame.K_UP: # ARROW UP
                        if selected_option > 0:
                            selected_option -= 1
                    if event.key == pygame.K_RETURN: # ENTER
                        return MENU_OPTIONS[selected_option]


    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont("impact", text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(text_surf, text_rect)