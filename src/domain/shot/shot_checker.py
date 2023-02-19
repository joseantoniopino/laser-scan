from datetime import datetime, timedelta
from typing import Optional, Tuple


class ShotChecker:
    def __init__(self, wait_times: Tuple[timedelta, timedelta, timedelta]) -> None:
        self.wait_times = wait_times

    def can_fire(self, last_shot: Optional[datetime]) -> Tuple[bool, Optional[int]]:
        if last_shot is None:
            return True, None

        time_since_last_shot = datetime.utcnow() - last_shot
        wait_time = None

        for i, wt in enumerate(self.wait_times):
            if time_since_last_shot >= wt:
                break
            wait_time = wt - time_since_last_shot

        if wait_time is None:
            return True, None

        return False, wait_time.seconds
