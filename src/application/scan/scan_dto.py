from src.application.target.DTO.target_dto import TargetDTO
from src.application.laser.DTO.laser_dto import LaserDTO


class ScanDTO:
    def __init__(self, laser_dto: LaserDTO, target_dto: TargetDTO):
        self.laser = {
            "laser_id": laser_dto.laser_id,
            "last_fire": laser_dto.last_fire,
            "position": laser_dto.position,
        }
        self.target = {
            "target_id": target_dto.target_id,
            "faction": target_dto.faction,
            "ship_name": target_dto.ship_name,
            "position": target_dto.position,
        }

