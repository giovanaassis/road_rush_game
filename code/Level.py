import pygame

from code.Entity import Entity
from code.EntityFactory import EntityFactory


class Level:
    def __init__(self, window, name: str):
        self.window = window
        self.name = name
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity("RoadBg"))

    def run(self):
        clock = pygame.time.Clock()
        while True:
            for ent in self.entity_list:
                self.window.blit(ent.surf, ent.rect)
                ent.move()
            pygame.display.flip()
            clock.tick(60)
