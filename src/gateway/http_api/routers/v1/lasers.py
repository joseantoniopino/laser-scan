from typing import Dict

from fastapi import Depends, APIRouter
from starlette import status
from pydantic import BaseModel

from src.infrastructure.controllers.laser_controller import LaserController

router = APIRouter(prefix='/lasers')


class Coordinates(BaseModel):
    x: float
    y: float


@router.post(
    '/{laser_id}/aim',
    summary='Points the laser target to the given coordinates',
    status_code=status.HTTP_200_OK,
)
async def aim(laser_id: str, coordinates: Coordinates, laser_controller: LaserController = Depends()):
    x = coordinates.x
    y = coordinates.y
    return laser_controller.aim(laser_id, x, y)
    # return {'x': coordinates.x, 'y': coordinates.y}
