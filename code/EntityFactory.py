from code.Background import Background
from code.Const import WIN_HEIGHT


class EntityFactory:
    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
            match entity_name:
                case "RoadBg":
                    return [
                        Background("RoadBg", (0, 0)),
                        Background("RoadBg", (0, -WIN_HEIGHT))
                    ]
            return None
