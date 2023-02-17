from sqlalchemy import text

from src.application.interfaces.repositories.i_laser_repository import ILaserRepository
from src.infrastructure.db.session_manager import session_scope
from src.infrastructure.exceptions.infrastructure_exception import InfrastructureException


class LaserRepository(ILaserRepository):
    def find_by_id(self, laser_id: str):
        with session_scope() as session:
            query = text("SELECT * FROM lasers WHERE id = :laser_id LIMIT 1")
            result = session.execute(query, {'laser_id': laser_id})
            laser = result.fetchone()
        if laser is None:
            raise InfrastructureException(status_code=404, code="laser_not_found", detail="Laser not found with id: {}".format(laser_id))
        return laser
