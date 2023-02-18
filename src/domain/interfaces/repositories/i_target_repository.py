from abc import ABC, abstractmethod
from typing import List, Dict


class ITargetRepository(ABC):
    @abstractmethod
    def all(self) -> List[Dict[str, float]]:
        pass
