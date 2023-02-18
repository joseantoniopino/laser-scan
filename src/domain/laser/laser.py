from src.domain.common.value_objects import Coordinates
from datetime import datetime
from typing import Union


class Laser:
    def __init__(self, laser_id: str, origin: Coordinates, last_fire: Union[datetime, None]):
        self._laser_id = laser_id
        self._origin = origin
        self._last_fire = last_fire

    def get_laser_id(self):
        return self._laser_id

    def get_last_fire(self):
        return self._last_fire

    def get_origin(self):
        return self._origin

    def __str__(self):
        return f"Laser(laser_id={self._laser_id}, origin={self._origin}, last_fire={self._last_fire})"

    def __repr__(self):
        return self.__str__()
