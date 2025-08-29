from code.Const import WIN_HEIGHT, WIN_WIDTH
from code.Entity import Entity
from code.Traffic import Traffic


class EntityMediator:

    @staticmethod
    def __verify_collision_window(ent: Entity):
        if isinstance(ent, Traffic):
            if ent.rect.top > WIN_WIDTH:
                ent.health = 0

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            ent = entity_list[i]
            EntityMediator.__verify_collision_window(ent)

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.health <= 0:
                entity_list.remove(ent)