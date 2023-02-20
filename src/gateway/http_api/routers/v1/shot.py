from fastapi import Depends, APIRouter
from starlette import status

from src.infrastructure.controllers.shot_controller import ShotController

router = APIRouter(prefix='/shot')


@router.post(
    '/{laser_id}/{target_id}',
    summary='Give nearly _target and nearest _laser',
    status_code=status.HTTP_200_OK,
)
async def shot(laser_id: str, target_id: str, shot_controller: ShotController = Depends()):
    return shot_controller.shot(laser_id, target_id)
