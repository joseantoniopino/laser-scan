from typing import List, Dict

from src.domain.common.point import Point
from src.domain.common.value_objects import Coordinates
from src.domain.interfaces.repositories.i_laser_repository import ILaserRepository
from src.domain.interfaces.repositories.i_target_repository import ITargetRepository
from src.domain.laser.factories.laser_factory import LaserFactory
from src.domain.target.factories.target_factory import TargetFactory


class AimService:
    def __init__(self, target_repository: ITargetRepository, laser_repository: ILaserRepository):
        self._target_repository = target_repository
        self._laser_repository = laser_repository

    def handle(self, laser_id: str, x: float, y: float):
        laser = self._laser_repository.find_by_id(laser_id)
        laser_entity = LaserFactory.create_laser(laser_id=laser['id'], x=laser['x'], y=laser['y'], last_fire=laser['last_fire'])
        available_targets = self._target_repository.all()
        for target in available_targets:
            target_entity = TargetFactory.create_target(target_id=target['id'], x=target['x'], y=target['y'])
            return target_entity
            # distance = Point.distance(laser_entity.get_origin(), target_entity.get_position())
        






