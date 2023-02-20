from datetime import datetime, timedelta
from src.domain.common.entity_factory import EntityFactory
from src.domain.interfaces.repositories.i_laser_repository import ILaserRepository
from src.domain.interfaces.repositories.i_target_repository import ITargetRepository
from src.domain.shot.shot_checker import ShotChecker


class Shot:
    def __init__(self, target_repository: ITargetRepository, laser_repository: ILaserRepository):
        self.shot_checker = ShotChecker((timedelta(minutes=1, seconds=45), timedelta(minutes=1), timedelta(seconds=30)))
        self.target_repository = target_repository
        self.laser_repository = laser_repository
        self.last_shot = None
        self.target = None
        self.laser = None

    def shot(self, laser_id: str, target_id: str):
        self.target = self.target_repository.find_by_id(target_id)
        laser_from_repository = self.laser_repository.find_by_id(laser_id)
        self.laser = EntityFactory.create_laser(
            laser_from_repository.get("id"),
            laser_from_repository.get("x"),
            laser_from_repository.get("y"),
            laser_from_repository.get("last_shot")
        )
        self.last_shot = self.laser.get_last_shot()

        # Verificar que el láser puede disparar
        can_fire, time_to_wait = self.shot_checker.can_fire(self.last_shot)
        if can_fire:
            # Actualizar el último disparo del láser
            self.laser_repository.update_laser_last_shot(laser_id, datetime.utcnow())
        can_fire
        return can_fire, time_to_wait, self.laser.get_laser_id(), self.target.get("id")
