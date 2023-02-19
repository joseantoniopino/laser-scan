from src.domain.interfaces.repositories.i_laser_repository import ILaserRepository
from src.domain.interfaces.repositories.i_target_repository import ITargetRepository
from src.domain.shot.shot import Shot


class ShotService:
    def __init__(self, target_repository: ITargetRepository, laser_repository: ILaserRepository):
        self.target_repository = target_repository
        self.laser_repository = laser_repository
        self._shot = Shot(self.target_repository, self.laser_repository)

    def handle(self, laser_id: str, target_id: str):
        return self._shot.shot(laser_id, target_id)
