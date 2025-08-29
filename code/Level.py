import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_HEIGHT, C_WHITE, EVENT_TRAFFIC, SPAWN_TIME
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator


class Level:
    def __init__(self, window, name: str):
        self.window = window
        self.name = name
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity("RoadBg"))
        self.entity_list.append(EntityFactory.get_entity("Car"))
        self.timeout = 20000  # 20 SECONDS
        pygame.time.set_timer(EVENT_TRAFFIC, SPAWN_TIME)

    def run(self):
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(ent.surf, ent.rect)
                ent.move()


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_TRAFFIC:
                    self.entity_list.append(EntityFactory.get_entity("Traffic"))


            self.level_text(20, f"Timeout: {self.timeout / 1000 :.1f}s", C_WHITE, (70, 30))
            self.level_text(20, f'entidades: {len(self.entity_list)}', C_WHITE, (60, WIN_HEIGHT - 20))
            pygame.display.flip()

            EntityMediator.verify_collision(self.entity_list)
            EntityMediator.verify_health(self.entity_list)

    def level_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont("impact", text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(text_surf, text_rect)
