from unittest import TestCase

from src.domain.common.value_objects import Coordinates


class TestCoordinates(TestCase):
    def test_coordinates_initialization(self):
        # Arrange
        x = 1
        y = 2

        # Act
        coordinates = Coordinates(x, y)

        # Assert
        self.assertEqual(coordinates.x, x)
        self.assertEqual(coordinates.y, y)

    def test_equality(self):
        # Arrange
        coordinate1 = Coordinates(0, 1)
        coordinate2 = Coordinates(0, 1)
        coordinate3 = Coordinates(1, 1)

        # Act
        result1 = coordinate1 == coordinate2
        result2 = coordinate1 == coordinate3

        # Assert
        self.assertTrue(result1)
        self.assertFalse(result2)

    def test_str_representation(self):
        # Arrange
        coordinates = Coordinates(5, 10)

        # Act
        result = str(coordinates)

        # Assert
        self.assertEqual(result, "(5, 10)")

    def test_repr(self):
        # Arrange
        x, y = 4.2, 3.6
        coordinates = Coordinates(x, y)

        # Act
        result = repr(coordinates)

        # Assert
        expected_result = f"({x}, {y})"
        self.assertEqual(result, expected_result)

