from typing import List, Dict, Union, Optional
from src.domain.common.point import Point
from src.domain.common.value_objects import Coordinates


class NearestObjectFinder:
    @staticmethod
    def get_nearest_object(
            position: Coordinates,
            objects: List[Dict[str, Union[str, float]]],
            x_key: str = 'x',
            y_key: str = 'y',
    ) -> Optional[Dict[str, Union[str, float]]]:
        nearest_object = None
        nearest_distance = float('inf')
        for obj in objects:
            obj_position = Coordinates(obj[x_key], obj[y_key])
            distance = Point.distance(position, obj_position)
            if distance < nearest_distance:
                nearest_distance = distance
                nearest_object = obj
        return nearest_object
