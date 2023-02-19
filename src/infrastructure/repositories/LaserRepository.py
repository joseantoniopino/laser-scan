import uuid
from datetime import datetime

from sqlalchemy import text

from src.domain.interfaces.repositories.i_laser_repository import ILaserRepository
from src.infrastructure.db.session_manager import session_scope
from src.infrastructure.exceptions.infrastructure_exception import InfrastructureException


class LaserRepository(ILaserRepository):
    def find_by_id(self, laser_id: str):
        with session_scope() as session:
            query = text("SELECT * FROM lasers WHERE id = :laser_id LIMIT 1")
            result = session.execute(query, {'laser_id': laser_id})
            laser = result.fetchone()
        if laser is None:
            raise InfrastructureException(status_code=404, code="laser_not_found", detail="Laser not found with target_id: {}".format(laser_id))
        laser_dict = {
            'id': str(laser[0]),
            'x': laser[1],
            'y': laser[2],
            'last_shot': laser[3]
        }
        return laser_dict

    def all(self):
        with session_scope() as session:
            query = text("SELECT * FROM lasers")
            result = session.execute(query)
            lasers = result.fetchall()
        return [{"id": str(laser[0]), "x": float(laser[1]), "y": float(laser[2]), "last_shot": datetime(laser[3]) if laser[3] is not None else None} for laser in lasers]

    def update_laser_last_shot(self, laser_id: str, last_shot: datetime):
        with session_scope() as session:
            query = text("UPDATE lasers SET last_shot = :last_shot WHERE id = :laser_id")
            result = session.execute(query, {"last_shot": last_shot, "laser_id": laser_id})
            if result.rowcount == 0:
                raise InfrastructureException(status_code=404, code="laser_not_found", detail="Laser not found with id: {}".format(laser_id))