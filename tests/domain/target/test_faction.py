from unittest import TestCase

from src.domain.common.faction import Faction


class TestFaction(TestCase):

    def setUp(self) -> None:
        self.faction = Faction
        self.imperial_faction = self.faction.IMPERIAL
        self.rebel_faction = self.faction.REBEL

    def test_ship_names(self):
        # Arrange
        imperial_faction = self.imperial_faction
        rebel_faction = self.rebel_faction

        # Act
        imperial_ship_names = imperial_faction.ship_names
        rebel_ship_names = rebel_faction.ship_names

        # Assert
        self.assertIsInstance(imperial_ship_names, list)
        self.assertEqual(len(imperial_ship_names), 5)
        self.assertIn("TIE Fighter", imperial_ship_names)
        self.assertIn("TIE Interceptor", imperial_ship_names)
        self.assertIn("TIE Bomber", imperial_ship_names)
        self.assertIn("TIE Advanced x1", imperial_ship_names)
        self.assertIn("TIE Defender", imperial_ship_names)

        self.assertIsInstance(rebel_ship_names, list)
        self.assertEqual(len(rebel_ship_names), 5)
        self.assertIn("X-Wing", rebel_ship_names)
        self.assertIn("Y-Wing", rebel_ship_names)
        self.assertIn("A-Wing", rebel_ship_names)
        self.assertIn("B-Wing", rebel_ship_names)
        self.assertIn("U-Wing", rebel_ship_names)

        self.assertNotEqual(imperial_ship_names, rebel_ship_names)

    def test_ship_names_are_unique(self):
        # Arrange
        imperial_faction = self.imperial_faction
        rebel_faction = self.rebel_faction

        # Act
        imperial_ship_names = imperial_faction.ship_names
        rebel_ship_names = rebel_faction.ship_names

        # Assert
        self.assertEqual(len(set(imperial_ship_names)), len(imperial_ship_names))
        self.assertEqual(len(set(rebel_ship_names)), len(rebel_ship_names))

        self.assertEqual(len(set(imperial_ship_names + rebel_ship_names)), len(imperial_ship_names + rebel_ship_names))

    def test_faction_values(self):
        self.assertEqual(Faction.IMPERIAL.value, "Imperial")
        self.assertEqual(Faction.REBEL.value, "Rebel")
