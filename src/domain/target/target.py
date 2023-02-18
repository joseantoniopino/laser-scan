from src.domain.common.value_objects import Coordinates
from src.domain.target.ship_generator import ShipGenerator


class Target:
    def __init__(self, target_id: str, position: Coordinates) -> None:
        self._target_id = target_id
        self._faction, self._name = ShipGenerator().generate()
        self._position = position

    def get_target_id(self) -> str:
        return self._target_id

    def get_faction(self) -> str:
        return self._faction

    def get_name(self) -> str:
        return self._name

    def get_position(self) -> Coordinates:
        return self._position

    def __str__(self) -> str:
        return f"Target(faction='{self._faction}', name='{self._name}', position={self._position})"

    def __repr__(self) -> str:
        return self.__str__()
