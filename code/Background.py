from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Entity import Entity


class Background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        self.rect.y += self.speed
        if self.rect.top >= WIN_HEIGHT:
            self.rect.y = -WIN_HEIGHT