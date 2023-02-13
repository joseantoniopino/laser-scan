import math
from src.domain.common.value_objects import Coordinates


class Point:
    @staticmethod
    def distance(coord1: Coordinates, coord2: Coordinates):
        x1, y1 = coord1.get_x(), coord1.get_y()
        x2, y2 = coord2.get_x(), coord2.get_y()
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
