from typing import List, Dict, Union

from sqlalchemy import text

from src.infrastructure.db.session_manager import session_scope
from src.domain.interfaces.repositories.i_target_repository import ITargetRepository
from src.infrastructure.exceptions.infrastructure_exception import InfrastructureException


class TargetRepository(ITargetRepository):
    def all(self):
        with session_scope() as session:
            query = text("SELECT * FROM targets")
            result = session.execute(query)
            targets = result.fetchall()
        return [{"id": str(target[0]), "x": float(target[1]), "y": float(target[2])} for target in targets]

    def find_by_id(self, target_id: str) -> Dict[str, Union[str, float]]:
        with session_scope() as session:
            query = text("SELECT * FROM targets WHERE id = :target_id LIMIT 1")
            result = session.execute(query, {'target_id': target_id})
            target = result.fetchone()
        if target is None:
            raise InfrastructureException(status_code=404, code="target_not_found", detail="Target not found with target_id: {}".format(target_id))
        target_dict = {
            'id': str(target[0]),
            'x': target[1],
            'y': target[2]
        }
        return target_dict
