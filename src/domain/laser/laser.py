from src.domain.common.value_objects import Coordinates
from src.domain.laser.interfaces.i_laser_shot import ILaserShot
from src.domain.target.target import Target


class Laser:
    def __init__(self, origin: Coordinates, target: Target, shot: ILaserShot):
        self._origin = origin
        self._target = target
        self._shot = shot

    def get_origin(self):
        return self._origin

    def get_target(self):
        return self._target

    def fire(self):
        return self._shot.fire()

    def __str__(self):
        return f"Laser(origin={self._origin}, target={self._target}, last_fire={self._last_fire})"

    def __repr__(self):
        return self.__str__()
