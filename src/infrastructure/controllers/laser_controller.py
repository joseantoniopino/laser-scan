from src.application.aim.aim_service import AimService
from src.infrastructure.repositories.LaserRepository import LaserRepository
from src.infrastructure.repositories.TargetRepository import TargetRepository
from src.infrastructure.requests.aim_request import AimRequest


class LaserController:
    def __init__(self):
        self.aim_request = AimRequest
        self.laser_repository = LaserRepository()
        self.target_repository = TargetRepository()
        self.aim_service = AimService(self.target_repository, self.laser_repository)

    def aim(self, laser_id: str, x: float, y: float):
        aim_request = self.aim_request(laser_id, x, y)
        return self.aim_service.handle(laser_id, x, y)
        # return {'laser_id': aim_request.laser_id, 'x': aim_request.x, 'y': aim_request.y}
