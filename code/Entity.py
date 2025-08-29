from abc import ABC, abstractmethod

import pygame.image

from code.Const import ENTITY_SPEED


class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = pygame.image.load("./assets/" + name + ".png")
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = ENTITY_SPEED[self.name]
        self.health = 1

    @abstractmethod
    def move(self):
        pass