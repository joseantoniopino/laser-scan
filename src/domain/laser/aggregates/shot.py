from datetime import datetime, timedelta
from math import sqrt

from src.domain.common.faction import Faction
from src.domain.common.value_objects import Coordinates
from src.domain.laser.interfaces.i_laser_shot import ILaserShot
from src.domain.target.target import Target


class Shot(ILaserShot):
    def __init__(self, origin: Coordinates, target: Target):
        self._origin = origin
        self._last_fire = None
        self._target = target
        self._target_position = target.get_position()
        self._distance = self._calculate_distance()
        self._reload_time = self._calculate_reload_time()

    def fire(self):
        if not self._target:
            raise Exception("No hay blanco seleccionado.")
        if self._target.get_faction() == Faction.REBEL.value:
            raise Exception("No se puede apuntar a un blanco amigo.")
        if self._last_fire and not self._can_fire():
            raise Exception("El laser aún no se ha recargado.")
        reload_time = self._reload_time
        self._last_fire = datetime.now()
        print(f"El laser ha sido disparado desde {self._origin} "
              f"hacia el blanco {self._target.get_name()} en "
              f"{self._target.get_position()}. Tiempo de recarga: {reload_time}")

    def _can_fire(self):
        return datetime.now() >= self._last_fire + self._reload_time()

    def _calculate_reload_time(self) -> timedelta:
        if self._distance < 10:
            return timedelta(seconds=30)
        elif 10 <= self._distance < 50:
            return timedelta(seconds=60)
        elif 50 <= self._distance <= 100:
            return timedelta(seconds=105)
        else:
            raise Exception("El laser solo puede disparar hasta 100 unidades astronómicas.")

    def _calculate_distance(self) -> float:
        origin_x = self._origin.get_x()
        origin_y = self._origin.get_y()
        target_x = self._target_position.get_x()
        target_y = self._target_position.get_y()
        return sqrt((target_x - origin_x) ** 2 + (target_y - origin_y) ** 2)
