from unittest import TestCase

from src.domain.target.faction import Faction
from src.domain.target.target import Target
from src.domain.common.value_objects import Coordinates


class TestTarget(TestCase):

    def setUp(self) -> None:
        self.position = Coordinates(0, 0)
        self.target = Target(self.position)

    def test_get_faction(self):
        # Arrange
        target = self.target

        # Act
        result = target.get_faction()

        # Assert
        self.assertIsInstance(result, str)
        self.assertIn(result, [f.value for f in Faction])
        self.assertEqual(result, target.get_faction())
        self.assertGreater(len(result), 0)

    def test_get_name(self):
        # Arrange
        target = self.target

        # Act
        result = target.get_name()

        # Assert
        self.assertIsInstance(result, str)
        self.assertIn(result, [ship for f in Faction for ship in f.ship_names])

    def test_get_position(self):
        # Arrange
        position = self.position
        target = self.target

        # Act
        result = target.get_position()

        # Assert
        self.assertIsInstance(result, Coordinates)
        self.assertEqual(result, position)
