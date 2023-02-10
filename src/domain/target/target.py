from src.domain.common.value_objects import Coordinates
from src.domain.target import ShipGenerator


class Target:
    def __init__(self, position: Coordinates):
        self.faction, self.name = ShipGenerator().generate()
        self.position = position

    def __str__(self):
        return f"Target(faction = '{self.faction}' ,name='{self.name}', position={self.position})"

    def __repr__(self):
        return self.__str__()
