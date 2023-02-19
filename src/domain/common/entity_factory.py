from datetime import datetime
from typing import Optional

from src.domain.common.value_objects import Coordinates
from src.domain.laser.laser import Laser
from src.domain.target.target import Target


class EntityFactory:
    @staticmethod
    def create_target(target_id: str, x: float, y: float) -> Target:
        position = Coordinates(x, y)
        return Target(target_id=target_id, position=position)

    @staticmethod
    def create_laser(laser_id: str, x: float, y: float, last_fire: Optional[datetime]) -> Laser:
        position = Coordinates(x, y)
        return Laser(laser_id=laser_id, position=position, last_fire=last_fire)
