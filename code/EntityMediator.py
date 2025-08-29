from code.Const import WIN_HEIGHT, WIN_WIDTH
from code.Entity import Entity
from code.Player import Player
from code.Traffic import Traffic


class EntityMediator:

    @staticmethod
    def __verify_collision_window(ent: Entity):
        if isinstance(ent, Traffic):
            if ent.rect.top > WIN_WIDTH:
                ent.health = 0

    @staticmethod
    def __verify_collision_entity(ent1, ent2):
        valid_interaction = False
        if isinstance(ent1, Player) and isinstance(ent2, Traffic):
            valid_interaction = True
        elif isinstance(ent1, Traffic) and isinstance(ent2, Player):
            valid_interaction = True

        if valid_interaction:
            if ent1.rect.colliderect(ent2.rect):
                ent1.health = 0
                ent2.health = 0


    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            ent1 = entity_list[i]
            EntityMediator.__verify_collision_window(ent1)
            for j in range(i + 1, len(entity_list)):
                ent2 = entity_list[j]
                EntityMediator.__verify_collision_entity(ent1, ent2)

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.health <= 0:
                entity_list.remove(ent)