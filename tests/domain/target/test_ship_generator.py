from unittest import TestCase

from src.domain.common.faction import Faction
from src.domain.target.ship_generator import ShipGenerator


class TestShipGenerator(TestCase):

    def setUp(self) -> None:
        self.ship_generator = ShipGenerator()

    def test_generate(self):
        # Arrange
        ship_generator = self.ship_generator

        # Act
        faction, name = ship_generator.generate()

        # Assert
        assert isinstance(faction, str)
        assert isinstance(name, str)

    def test_faction_value(self):
        # Arrange
        ship_generator = self.ship_generator

        # Act
        faction, name = ship_generator.generate()

        # Assert
        self.assertIn(faction, [Faction.IMPERIAL.value, Faction.REBEL.value])

    def test_ship_name(self):
        # Arrange
        ship_generator = self.ship_generator

        # Act
        faction, name = ship_generator.generate()
        faction_obj = Faction(faction)

        # Assert
        self.assertIn(name, faction_obj.ship_names)
