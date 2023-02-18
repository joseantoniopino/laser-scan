class LaserDTO:
    def __init__(self, laser_id: str, x: float, y: float, last_fire: str):
        self.laser_id = laser_id
        self.last_fire = last_fire
        self.position = {
            "x": x,
            "y": y
        }
