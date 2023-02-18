class TargetDTO:
    def __init__(self, target_id: str, faction: str, name: str, x: float, y: float):
        self.target_id = target_id
        self.faction = faction
        self.ship_name = name
        self.position = {
            "x": x,
            "y": y
        }
