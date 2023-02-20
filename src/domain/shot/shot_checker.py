from datetime import datetime, timedelta
from typing import Optional, Tuple


class ShotChecker:
    @staticmethod
    def can_fire(last_shot: Optional[datetime]) -> Tuple[bool, Optional[int]]:
        if last_shot is None:
            return True, None

        time_since_last_shot = datetime.utcnow() - last_shot
        wait_time = None

        if time_since_last_shot < timedelta(seconds=30):
            wait_time = timedelta(seconds=30) - time_since_last_shot
        elif time_since_last_shot < timedelta(minutes=1):
            wait_time = timedelta(minutes=1) - time_since_last_shot
        elif time_since_last_shot <= timedelta(minutes=1, seconds=45):
            wait_time = timedelta(minutes=1, seconds=45) - time_since_last_shot

        if wait_time is None:
            return True, None

        return False, wait_time.seconds
