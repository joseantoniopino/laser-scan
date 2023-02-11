class Coordinates:
    def __init__(self, x: float, y: float):
        self._x = x
        self._y = y

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def __eq__(self, other):
        if isinstance(other, Coordinates):
            return self._x == other._x and self._y == other._y
        return False

    def __str__(self):
        return f"({self._x}, {self._y})"

    def __repr__(self):
        return self.__str__()
