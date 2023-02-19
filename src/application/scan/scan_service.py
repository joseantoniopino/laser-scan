from src.application.scan.scan_response import ScanResponse
from src.domain.interfaces.repositories.i_laser_repository import ILaserRepository
from src.domain.interfaces.repositories.i_target_repository import ITargetRepository
from src.domain.scanner.scanner import Scanner


class ScanService:
    def __init__(self, target_repository: ITargetRepository, laser_repository: ILaserRepository):
        self._target_repository = target_repository
        self._laser_repository = laser_repository
        self._scanner = Scanner(target_repository, laser_repository)
        self._scan_response = ScanResponse()

    def handle(self, x: float, y: float):
        laser_entity, target_entity = self._scanner(x, y)
        return self._scan_response.format(laser_entity, target_entity)
