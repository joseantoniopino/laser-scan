from sqlalchemy import text

from src.domain.common.point import Point
from src.domain.common.value_objects import Coordinates
from src.infrastructure.db.session_manager import session_scope
from src.application.interfaces.repositories.i_target_repository import ITargetRepository


class TargetRepository(ITargetRepository):
    def find_nearest(self, x, y):
        origin = Coordinates(x, y)
        with session_scope() as session:
            query = text("SELECT * FROM targets")
            result = session.execute(query)
            targets = result.fetchall()
        nearest_target = None
        nearest_distance = float("inf")
        for target in targets:
            target_coordinates = Coordinates(target.x, target.y)
            distance = Point(origin, target_coordinates).distance()
            if distance < nearest_distance:
                nearest_target = target
                nearest_distance = distance
        return nearest_target
