import random

from src.domain.target.faction import Faction


class ShipGenerator:
    @classmethod
    def generate(cls) -> (str, str):
        faction = random.choice([Faction.IMPERIAL, Faction.REBEL])
        return faction.value, random.choice(faction.ship_names)

