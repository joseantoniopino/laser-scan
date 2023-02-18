from typing import List, Dict, Union

from sqlalchemy import text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.types import CHAR, VARCHAR

from src.infrastructure.db.session_manager import session_scope
from src.domain.interfaces.repositories.i_target_repository import ITargetRepository


class TargetRepository(ITargetRepository):
    def all(self):
        with session_scope() as session:
            query = text("SELECT * FROM targets")
            result = session.execute(query)
            targets = result.fetchall()
        return [{"id": str(target[0]), "x": float(target[1]), "y": float(target[2])} for target in targets]
