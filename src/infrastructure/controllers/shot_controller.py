from src.application.shot.shot_service import ShotService
from src.infrastructure.repositories.LaserRepository import LaserRepository
from src.infrastructure.repositories.TargetRepository import TargetRepository
from src.infrastructure.requests.shot_request import ShotRequest


class ShotController:
    def __init__(self):
        self.shot_request = ShotRequest
        self.shot_service = ShotService()

    def shot(self, laser_id: str, target_id: str):
        shot_request = self.shot_request(laser_id, target_id)
        return self.shot_service.handle(shot_request.laser_id, shot_request.target_id)
