import random

from src.domain.common.faction import Faction


class ShipGenerator:
    @classmethod
    def generate(cls) -> (str, str):
        faction = random.choice([faction for faction in Faction])
        return faction.value, random.choice(faction.ship_names)

