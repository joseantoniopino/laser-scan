class ShotResponse:
    @staticmethod
    def format(laser_id: str, target_id: str, success: bool, time_to_wait: int, message: str = "") -> dict:
        return {
            "message": message,
            "laser_id": laser_id,
            "target_id": target_id,
            "success": success,
            "time_to_wait": time_to_wait
        }
