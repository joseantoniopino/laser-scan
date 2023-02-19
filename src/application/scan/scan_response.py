from src.domain.laser.laser import Laser
from src.domain.target.target import Target


class ScanResponse:
    @staticmethod
    def format(laser: Laser, target: Target) -> dict:
        return {
            "laser": {
                "laser_id": laser.get_laser_id(),
                "last_shot": laser.get_last_shot(),
                "position": {
                    "x": laser.get_position().get_x(),
                    "y": laser.get_position().get_y()
                }
            },
            "target": {
                "target_id": target.get_target_id(),
                "faction": target.get_faction(),
                "ship_name": target.get_name(),
                "position": {
                    "x": target.get_position().get_x(),
                    "y": target.get_position().get_y()
                }
            }
        }
