import uuid

from src.infrastructure.exceptions.infrastructure_exception import InfrastructureException


class ScanRequest:
    def __init__(self, x: float, y: float):
        if not isinstance(x, float) or x > 100 or x < 0:
            raise InfrastructureException(status_code=422, code="invalid_x", detail="x must be a float between 0 and 100 (inclusive)")
        if not isinstance(y, float) or y > 100 or y < 0:
            raise InfrastructureException(status_code=422, code="invalid_y", detail="y must be a float between 0 and ")

        self.x = x
        self.y = y
