from abc import ABC, abstractmethod


class ILaserShot(ABC):
    @abstractmethod
    def fire(self):
        pass

    @abstractmethod
    def get_last_fire(self):
        pass
