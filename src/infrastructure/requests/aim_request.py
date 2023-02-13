import uuid

from src.infrastructure.exceptions.infrastructure_exception import InfrastructureException


class AimRequest:
    def __init__(self, laser_id: str, x: float, y: float):
        if not isinstance(laser_id, str):
            raise InfrastructureException(status_code=422, code="invalid_laser_id", detail="laser_id must be a string")
        if not isinstance(x, float) or x > 100 or x < 0:
            raise InfrastructureException(status_code=422, code="invalid_x", detail="x must be a float between 0 and 100 (inclusive)")
        if not isinstance(y, float) or y > 100 or y < 0:
            raise InfrastructureException(status_code=422, code="invalid_y", detail="y must be a float between 0 and ")
        try:
            uuid.UUID(laser_id)
        except InfrastructureException:
            raise InfrastructureException(status_code=422, code="invalid_laser_id", detail="laser_id must be a valid UUID")

        self.laser_id = laser_id
        self.x = x
        self.y = y
