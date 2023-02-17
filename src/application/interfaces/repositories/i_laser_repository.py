from abc import ABC, abstractmethod


class ILaserRepository(ABC):
    @abstractmethod
    def find_by_id(self, laser_id: str):
        pass
