import random

from code.Background import Background
from code.Const import WIN_HEIGHT, WIN_WIDTH, TRAFFIC_POSITIONS
from code.Player import Player
from code.Traffic import Traffic

last_pos = None

class EntityFactory:
    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        global last_pos
        match entity_name:
            case "RoadBg":
                return [
                    Background("RoadBg", (0, 0)),
                    Background("RoadBg", (0, -WIN_HEIGHT))
                ]
            case "Car":
                return Player("Car", (275, WIN_HEIGHT - 120))
            case "Traffic":
                pos_x = random.choice([p for p in TRAFFIC_POSITIONS if p != last_pos])
                last_pos = pos_x
                return Traffic("Traffic", (pos_x, -170))
        return None
