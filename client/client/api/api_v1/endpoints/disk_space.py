from fastapi import APIRouter

from client.controllers.disk_space import alert_for_disk_usage

router = APIRouter()


@router.get("/disk_space")
async def disk_space():
    return alert_for_disk_usage("/", 20182291968)
