from fastapi import APIRouter

from client.controllers.disk_space import alert_for_disk_usage
from client.core.constants import DigitalInfoEnum
from client.schemas.schema_vitals import DiskSpaceSchema

router = APIRouter()


@router.get("/check")
async def disk_space(threshold_gb: float = 20) -> DiskSpaceSchema:
    return alert_for_disk_usage("/", threshold_gb * DigitalInfoEnum.gb)
