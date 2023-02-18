from typing import List, Dict, Union, Optional

from src.application.scan.scan_dto import ScanDTO
from src.application.laser.DTO.laser_dto import LaserDTO
from src.application.target.DTO.target_dto import TargetDTO
from src.domain.common.point import Point
from src.domain.common.value_objects import Coordinates
from src.domain.interfaces.repositories.i_laser_repository import ILaserRepository
from src.domain.interfaces.repositories.i_target_repository import ITargetRepository
from src.domain.laser.factories.laser_factory import LaserFactory
from src.domain.target.factories.target_factory import TargetFactory


class ScanService:
    def __init__(self, target_repository: ITargetRepository, laser_repository: ILaserRepository):
        self._target_repository = target_repository
        self._laser_repository = laser_repository

    def handle(self, x: float, y: float):
        available_targets = self._target_repository.all()
        available_lasers = self._laser_repository.all()
        laser_dto = None
        target_dto = None
        while available_targets:
            nearest_target = self._get_nearest_object(Coordinates(x, y), available_targets)
            target_entity = TargetFactory.create_target(
                target_id=nearest_target['id'],
                x=nearest_target['x'],
                y=nearest_target['y'],
            )
            target_entity_faction = target_entity.get_faction()
            if target_entity_faction == 'Rebel':
                available_targets.remove(nearest_target)
            else:
                nearest_laser = self._get_nearest_object(target_entity.get_position(), available_lasers)
                laser_entity = LaserFactory.create_laser(
                    laser_id=nearest_laser['id'],
                    x=nearest_laser['x'],
                    y=nearest_laser['y'],
                    last_fire=nearest_laser.get('last_fire')
                )
                laser_dto = LaserDTO(
                    laser_id=laser_entity.get_laser_id(),
                    last_fire=laser_entity.get_last_fire(),
                    x=laser_entity.get_position().get_x(),
                    y=laser_entity.get_position().get_y()
                )
                target_dto = TargetDTO(
                    target_id=target_entity.get_target_id(),
                    faction=target_entity.get_faction(),
                    name=target_entity.get_name(),
                    x=target_entity.get_position().get_x(),
                    y=target_entity.get_position().get_y()
                )
                break
        return ScanDTO(laser_dto, target_dto)

    @staticmethod
    def _get_nearest_object(
            position: Coordinates,
            objects: List[Dict[str, Union[str, float]]],
            x_key: str = 'x',
            y_key: str = 'y',
    ) -> Optional[Dict[str, Union[str, float]]]:
        nearest_object = None
        nearest_distance = float('inf')
        for obj in objects:
            obj_position = Coordinates(obj[x_key], obj[y_key])
            distance = Point.distance(position, obj_position)
            if distance < nearest_distance:
                nearest_distance = distance
                nearest_object = obj
        return nearest_object

