from abc import ABC, abstractmethod


class ILaserShot(ABC):
    @abstractmethod
    def fire(self):
        pass
