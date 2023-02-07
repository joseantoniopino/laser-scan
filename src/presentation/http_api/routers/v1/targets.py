from fastapi import APIRouter

router = APIRouter(prefix='/targets')


@router.get('/')
async def get_targets():
    return {'targets': 'targets'}
