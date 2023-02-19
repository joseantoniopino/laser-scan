from src.domain.common.point import Point
from src.domain.common.value_objects import Coordinates
from datetime import datetime, timedelta
from typing import Union


class Laser:
    def __init__(self, laser_id: str, position: Coordinates, last_shot: Union[datetime, None]):
        self._laser_id = laser_id
        self._position = position
        self._last_shot = last_shot

    def get_laser_id(self):
        return self._laser_id

    def get_last_shot(self):
        return self._last_shot

    def get_position(self):
        return self._position

    def is_loaded(self) -> bool:
        if self._last_shot is None:
            return True
        time_since_last_shot = datetime.utcnow() - self._last_shot
        if self.get_reload_time() <= time_since_last_shot:
            return True
        else:
            return False

    def get_reload_time(self) -> timedelta:
        distance = Point.distance(self._position, Coordinates(0, 0))
        if distance < 10:
            reload_time = timedelta(seconds=30)
        elif distance < 50:
            reload_time = timedelta(minutes=1)
        else:
            reload_time = timedelta(minutes=1, seconds=45)
        return reload_time

    def __str__(self):
        return f"Laser(laser_id={self._laser_id}, origin={self._position}, last_fire={self._last_shot})"

    def __repr__(self):
        return self.__str__()
