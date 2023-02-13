from fastapi import APIRouter
from starlette import status
from starlette.responses import Response

router = APIRouter(prefix='/lasers')


@router.post(
    '/{laser_id}/x/y/aim',
    summary='Points the laser target to the given coordinates',
    status_code=status.HTTP_204_NO_CONTENT
)
async def aim(laser_id: str, x: float, y: float):
    pass

