from src.domain.interfaces.repositories.i_laser_repository import ILaserRepository
from src.domain.interfaces.repositories.i_target_repository import ITargetRepository
from src.domain.scanner.scanner import Scanner


class ScanService:
    def __init__(self, target_repository: ITargetRepository, laser_repository: ILaserRepository):
        self._target_repository = target_repository
        self._laser_repository = laser_repository
        self._scanner = Scanner(target_repository, laser_repository)

    def handle(self, x: float, y: float):
        return self._scanner(x, y)



