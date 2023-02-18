from src.application.scan.scan_service import ScanService
from src.infrastructure.repositories.LaserRepository import LaserRepository
from src.infrastructure.repositories.TargetRepository import TargetRepository
from src.infrastructure.requests.scan_request import ScanRequest


class ScanController:
    def __init__(self):
        self.scan_request = ScanRequest
        self.laser_repository = LaserRepository()
        self.target_repository = TargetRepository()
        self.scan_service = ScanService(self.target_repository, self.laser_repository)

    def scan(self, x: float, y: float):
        scan_request = self.scan_request(x, y)
        return self.scan_service.handle(scan_request.x, scan_request.y)
