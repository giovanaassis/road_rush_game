import random

from code.Background import Background
from code.Const import WIN_HEIGHT, WIN_WIDTH, TRAFFIC_POSITIONS
from code.Player import Player
from code.Traffic import Traffic


class EntityFactory:
    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case "RoadBg":
                return [
                    Background("RoadBg", (0, 0)),
                    Background("RoadBg", (0, -WIN_HEIGHT))
                ]
            case "Car":
                return Player("Car", (275, WIN_HEIGHT - 120))
            case "Traffic":
                last_pos = None
                pos_x = random.choice([p for p in TRAFFIC_POSITIONS if p != last_pos])
                last_pos = pos_x
                return Traffic("Traffic", (pos_x, WIN_WIDTH - 100))
        return None
