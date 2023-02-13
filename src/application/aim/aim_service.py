from src.application.interfaces.repositories.i_target_repository import ITargetRepository
from src.application.laser.create_laser import create, CreateLaser
from src.domain.common.value_objects import Coordinates
from src.domain.target.target import Target


class AimService:
    def __init__(self, target_repository: ITargetRepository):
        self._target_repository = target_repository

    def handle(self):
        nearest_target = self.__find_nearest_target(0, 0)
        target = Target(id=nearest_target.id, position=Coordinates(x=nearest_target.x, y=nearest_target.y))
        laser = CreateLaser().create(target)

    def __find_nearest_target(self, x, y):
        target = self._target_repository.find_nearest(x, y)
        return target
