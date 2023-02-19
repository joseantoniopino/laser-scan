from abc import ABC, abstractmethod
from datetime import datetime
from typing import Optional
from src.domain.target.target import Target
from src.domain.laser.laser import Laser


class IEntityFactory(ABC):
    @staticmethod
    @abstractmethod
    def create_target(target_id: str, x: float, y: float) -> Target:
        pass

    @staticmethod
    @abstractmethod
    def create_laser(laser_id: str, x: float, y: float, last_fire: Optional[datetime]) -> Laser:
        pass
