from code.Const import WIN_HEIGHT
from code.Entity import Entity


class Traffic(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        self.rect.y += self.speed