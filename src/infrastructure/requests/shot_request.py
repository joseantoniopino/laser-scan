import uuid

from src.infrastructure.exceptions.infrastructure_exception import InfrastructureException


class ShotRequest:
    def __init__(self, laser_id: str, target_id: str):
        try:
            self.laser_id = uuid.UUID(laser_id)
        except ValueError:
            raise InfrastructureException(
                status_code=400,
                code='invalid_laser_id',
                detail=f'The provided laser ID ({laser_id}) is not a valid UUID.'
            )

        try:
            self.target_id = uuid.UUID(target_id)
        except ValueError:
            raise InfrastructureException(
                status_code=400,
                code='invalid_target_id',
                detail=f'The provided target ID ({target_id}) is not a valid UUID.'
            )
        self.laser_id = laser_id
        self.target_id = target_id
