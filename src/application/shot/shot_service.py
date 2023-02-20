from src.application.shot.shot_response import ShotResponse
from src.domain.common.entity_factory import EntityFactory
from src.domain.shot.shot import Shot
from src.infrastructure.repositories.LaserRepository import LaserRepository
from src.infrastructure.repositories.TargetRepository import TargetRepository


class ShotService:
    def __init__(self):
        self._entity_factory = EntityFactory()
        self._target_repository = TargetRepository()
        self._laser_repository = LaserRepository()
        self._shot = Shot(self._target_repository, self._laser_repository, self._entity_factory)

    def handle(self, laser_id: str, target_id: str):
        success, time_to_wait, laser_id, target_id = self._shot.shot(laser_id, target_id)
        if success:
            message = "El disparo fue exitoso"
        else:
            message = "Aún no puedes disparar"
        return ShotResponse.format(laser_id, target_id, success, time_to_wait, message)





