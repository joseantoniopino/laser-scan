from src.application.shot.shot_response import ShotResponse
from src.domain.interfaces.repositories.i_laser_repository import ILaserRepository
from src.domain.interfaces.repositories.i_target_repository import ITargetRepository
from src.domain.shot.shot import Shot


class ShotService:
    def __init__(self, target_repository: ITargetRepository, laser_repository: ILaserRepository):
        self.target_repository = target_repository
        self.laser_repository = laser_repository
        self._shot = Shot(self.target_repository, self.laser_repository)

    def handle(self, laser_id: str, target_id: str):
        success, time_to_wait, laser_id, target_id = self._shot.shot(laser_id, target_id)
        if success:
            message = "El disparo fue exitoso"
        else:
            message = "Aún no puedes disparar"
        return ShotResponse.format(laser_id, target_id, success, time_to_wait, message)





