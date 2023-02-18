from typing import Union
from datetime import datetime

from src.domain.common.value_objects import Coordinates
from src.domain.laser.laser import Laser


class LaserFactory:
    @staticmethod
    def create_laser(laser_id: str, x: float, y: float, last_fire: Union[datetime, None]) -> Laser:
        origin = Coordinates(x, y)
        return Laser(laser_id=laser_id, origin=origin, last_fire=last_fire)
