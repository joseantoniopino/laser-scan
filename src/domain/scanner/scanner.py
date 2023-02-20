from src.domain.common.value_objects import Coordinates
from src.domain.common.entity_factory import EntityFactory
from src.domain.common.NearestObjectFinder import NearestObjectFinder
from src.domain.interfaces.i_entity_factory import IEntityFactory
from src.domain.interfaces.repositories.i_laser_repository import ILaserRepository
from src.domain.interfaces.repositories.i_target_repository import ITargetRepository


class Scanner:
    def __init__(self, target_repository: ITargetRepository, laser_repository: ILaserRepository, entity_factory: IEntityFactory):
        self._target_repository = target_repository
        self._laser_repository = laser_repository
        self._nearest_object_finder = NearestObjectFinder()
        self.laser_entity = None
        self.target_entity = None

    def __call__(self, x: float, y: float):
        available_targets = self._target_repository.all()
        available_lasers = self._laser_repository.all()
        while available_targets:
            nearest_target = self._nearest_object_finder.get_nearest_object(Coordinates(x, y), available_targets)
            self.target_entity = EntityFactory.create_target(
                target_id=nearest_target['id'],
                x=nearest_target['x'],
                y=nearest_target['y'],
            )
            target_entity_faction = self.target_entity.get_faction()
            if target_entity_faction == 'Rebel':
                available_targets.remove(nearest_target)
            else:
                nearest_laser = self._nearest_object_finder.get_nearest_object(self.target_entity.get_position(), available_lasers)
                self.laser_entity = EntityFactory.create_laser(
                    laser_id=nearest_laser['id'],
                    x=nearest_laser['x'],
                    y=nearest_laser['y'],
                    last_fire=nearest_laser.get('last_shot')
                )
                break
        return self.laser_entity, self.target_entity
