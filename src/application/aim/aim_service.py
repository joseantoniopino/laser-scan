from src.application.interfaces.repositories.i_laser_repository import ILaserRepository
from src.application.interfaces.repositories.i_target_repository import ITargetRepository


class AimService:
    def __init__(self, target_repository: ITargetRepository, laser_repository: ILaserRepository):
        self._target_repository = target_repository
        self._laser_repository = laser_repository

    def handle(self, laser_id: str, x: float, y: float):
        laser = self._laser_repository.find_by_id(laser_id)
        target = self._target_repository.find_nearest(laser.x, laser.y)
        return {'target_id': target.id, 'x': target.x, 'y': target.y}

