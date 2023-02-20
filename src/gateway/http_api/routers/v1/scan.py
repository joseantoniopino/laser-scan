from fastapi import Depends, APIRouter
from starlette import status
from pydantic import BaseModel

from src.infrastructure.controllers.scan_controller import ScanController

router = APIRouter(prefix='/scan')


class Coordinates(BaseModel):
    x: float
    y: float


@router.get(
    '/',
    summary='Give nearly _target and nearest _laser',
    status_code=status.HTTP_200_OK,
)
async def scan(coordinates: Coordinates, scan_controller: ScanController = Depends()):
    x = coordinates.x
    y = coordinates.y
    return scan_controller.scan(x, y)
