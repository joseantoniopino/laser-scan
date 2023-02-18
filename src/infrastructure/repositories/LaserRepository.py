import uuid
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
            'last_fire': laser[3]
        }
        return laser_dict
