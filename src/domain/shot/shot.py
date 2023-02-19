from datetime import datetime, timedelta

from src.domain.common.entity_factory import EntityFactory
from src.domain.exceptions.domain_exception import DomainException
from src.domain.interfaces.repositories.i_laser_repository import ILaserRepository
from src.domain.interfaces.repositories.i_target_repository import ITargetRepository
from src.domain.laser.laser import Laser


class Shot:
    def __init__(self, target_repository: ITargetRepository, laser_repository: ILaserRepository):
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
        if self._check_laser_can_fire(self.laser):
            # Actualizar el último disparo del láser
            self.laser_repository.update_laser_last_shot(laser_id, datetime.utcnow())

            return f"El láser {laser_id} ha destruido el objetivo {target_id}"
        else:
            raise DomainException(status_code=403, code="forbidden",
                                  detail=f"Láser {laser_id} necesita esperar para disparar de nuevo")

    def _check_laser_can_fire(self, laser: Laser):
        if self.last_shot is None:
            return True

        time_since_last_shot = datetime.utcnow() - self.last_shot

        if time_since_last_shot >= timedelta(minutes=1, seconds=45):
            return True

        if time_since_last_shot >= timedelta(minutes=1):
            return True

        if time_since_last_shot >= timedelta(seconds=30):
            return True

        time_to_wait = 30 - time_since_last_shot.seconds
        raise DomainException(status_code=403, code="forbidden",
                              detail=f"Láser {laser.get_laser_id()} necesita esperar {time_to_wait} segundos para "
                                     f"disparar de nuevo")
