from src.domain.laser.laser import Laser
from src.domain.target.target import Target


class CreateLaser:
    def create(self, target: Target):
        return Laser(target)
