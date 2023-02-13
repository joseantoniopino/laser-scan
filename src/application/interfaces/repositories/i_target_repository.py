from abc import ABC, abstractmethod


class ITargetRepository(ABC):
    @abstractmethod
    def find_nearest(self, x, y):
        pass
