from datetime import datetime, timedelta
from src.domain.interfaces.i_entity_factory import IEntityFactory
from src.domain.interfaces.repositories.i_laser_repository import ILaserRepository
from src.domain.interfaces.repositories.i_target_repository import ITargetRepository
from src.domain.shot.shot_checker import ShotChecker


class Shot:
    def __init__(self, target_repository: ITargetRepository, laser_repository: ILaserRepository, entity_factory: IEntityFactory):
        self.shot_checker = ShotChecker()
        self._entity_factory = entity_factory
        self._target_repository = target_repository
        self._laser_repository = laser_repository
        self._last_shot = None
        self._target = None
        self._laser = None

    def shot(self, laser_id: str, target_id: str):
        self._target = self._target_repository.find_by_id(target_id)
        laser_from_repository = self._laser_repository.find_by_id(laser_id)
        self._laser = self._entity_factory.create_laser(
            laser_from_repository.get("id"),
            laser_from_repository.get("x"),
            laser_from_repository.get("y"),
            laser_from_repository.get("last_shot")
        )
        self._last_shot = self._laser.get_last_shot()

        can_fire, time_to_wait = self.shot_checker.can_fire(self._last_shot)

        if can_fire:
            self._laser_repository.update_laser_last_shot(laser_id, datetime.utcnow())
            # TODO: Eliminar el target de la base de datos
        return can_fire, time_to_wait, self._laser.get_laser_id(), self._target.get("id")

