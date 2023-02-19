from abc import ABC, abstractmethod
from datetime import datetime


class ILaserRepository(ABC):
    @abstractmethod
    def find_by_id(self, laser_id: str):
        pass

    @abstractmethod
    def all(self):
        pass

    @abstractmethod
    def update_laser_last_shot(self, laser_id: str, last_shot: datetime):
        pass
