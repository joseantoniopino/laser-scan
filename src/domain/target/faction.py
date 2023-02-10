from enum import Enum


class Faction(Enum):
    IMPERIAL = "Imperial"
    REBEL = "Rebel"

    @property
    def ship_names(self):
        if self == Faction.IMPERIAL:
            return [
                "TIE Fighter",
                "TIE Interceptor",
                "TIE Bomber",
                "TIE Advanced x1",
                "TIE Defender"
            ]
        elif self == Faction.REBEL:
            return [
                "X-Wing",
                "Y-Wing",
                "A-Wing",
                "B-Wing",
                "U-Wing"
            ]
