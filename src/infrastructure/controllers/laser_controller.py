from src.application.aim.aim_service import AimService


class LaserController:
    def __init__(self, aim_service: AimService):
        self.aim_service = aim_service

    def aim(self, laser_id: str, x: float, y: float):
        return self.aim_service.handle()
