import pygame

from code.Const import WIN_WIDTH
from code.Entity import Entity


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_LEFT] and self.rect.left > 95:
            self.rect.left -= self.speed
        if pressed_key[pygame.K_RIGHT] and self.rect.right < WIN_WIDTH - 95:
            self.rect.right += self.speed