from src.domain.common.value_objects import Coordinates
from src.domain.target.ship_generator import ShipGenerator


class Target:
    def __init__(self, id: str, position: Coordinates):
        self._id = id
        self._faction, self._name = ShipGenerator().generate()
        self._position = position

    def get_id(self):
        return self._id

    def get_faction(self):
        return self._faction

    def get_name(self):
        return self._name

    def get_position(self):
        return self._position

    def __str__(self):
        return f"Target(faction='{self._faction}', name='{self._name}', position={self._position})"

    def __repr__(self):
        return self.__str__()
