from src.application.scan.scan_response import ScanResponse
from src.domain.common.entity_factory import EntityFactory
from src.domain.scanner.scanner import Scanner
from src.infrastructure.repositories.LaserRepository import LaserRepository
from src.infrastructure.repositories.TargetRepository import TargetRepository


class ScanService:
    def __init__(self):
        self._target_repository = TargetRepository()
        self._laser_repository = LaserRepository()
        self._entity_factory = EntityFactory()
        self._scanner = Scanner(self._target_repository, self._laser_repository, self._entity_factory)
        self._scan_response = ScanResponse()

    def handle(self, x: float, y: float):
        laser_entity, target_entity = self._scanner(x, y)
        return self._scan_response.format(laser_entity, target_entity)
