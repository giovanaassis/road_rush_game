import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import C_LILAC, WIN_WIDTH, TUTORIAL_TEXT, C_WHITE


class Tutorial:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./assets/TutorialBg.png')
        self.rect = self.surf.get_rect()

    def run(self):
        while True:
            self.window.blit(self.surf, self.rect)

            self.tutorial_text(40, "TUTORIAL", C_LILAC, (WIN_WIDTH / 2, 80))
            for i in range(len(TUTORIAL_TEXT)):
                self.tutorial_text(30, TUTORIAL_TEXT[i], C_LILAC, (WIN_WIDTH / 2, 180 + i * 40))
            self.tutorial_text(20, "PRESS ENTER TO GO BACK", C_LILAC, (WIN_WIDTH / 2, 400))

            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit() # CLOSE THE WINDOW
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return False


    def tutorial_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont("impact", text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)

        padding = 6
        bg_rect = text_rect.inflate(padding * 2, padding * 2)
        pygame.draw.rect(self.window, C_WHITE, bg_rect)

        self.window.blit(text_surf, text_rect)