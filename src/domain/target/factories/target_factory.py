from src.domain.common.value_objects import Coordinates
from src.domain.target.target import Target


class TargetFactory:
    @staticmethod
    def create_target(target_id: str, x: float, y: float) -> Target:
        position = Coordinates(x, y)
        return Target(target_id=target_id, position=position)
