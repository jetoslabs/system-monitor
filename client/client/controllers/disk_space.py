import shutil
from typing import Tuple
from loguru import logger

from client.clients.nats import send_vitals
from client.core.constants import DigitalInfoEnum
from client.schemas.schema_vitals import DiskSpaceSchema, VitalsSchema


async def run():
    logger.bind().debug("disk usage...")
    diskspace: DiskSpaceSchema = alert_for_disk_usage("/", free_bytes=50*DigitalInfoEnum.gb)

    vitals = VitalsSchema(
        diskspace=diskspace
    )
    logger.bind(vitals=vitals).debug(f"vitals")

    # send vitals to NATS topic vitals, on alert
    if vitals and vitals.diskspace and vitals.diskspace.is_alert:
        await send_vitals(vitals)


def get_disk_usage(path: str) -> Tuple[int, int, int]:
    stat = shutil.disk_usage(path)
    # logger.bind(stat=stat).debug(f"get_disk_usage")
    return stat


def alert_for_disk_usage(path: str, free_bytes: int) -> DiskSpaceSchema:
    total, used, free = get_disk_usage(path)
    alert = False
    if free < free_bytes:
        alert = True

    diskspace = DiskSpaceSchema(
        is_alert=alert,
        total=total,
        used=used,
        free=free
    )
    return diskspace
