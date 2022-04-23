import shutil
from typing import Tuple
from loguru import logger

from client.core.constants import DigitalInfoEnum


def run():
    logger.bind().debug("disk usage...")
    is_alert, alert_msg = alert_for_disk_usage("/", free_bytes=20*DigitalInfoEnum.gb)
    logger.bind(is_alert=is_alert, alert_msg=alert_msg).debug(f"disk usage")


def get_disk_usage(path: str) -> Tuple[int, int, int]:
    stat = shutil.disk_usage(path)
    # logger.bind(stat=stat).debug(f"get_disk_usage")
    return stat


def alert_for_disk_usage(path: str, free_bytes: int) -> (bool, str):
    total, used, free = get_disk_usage(path)
    if free < free_bytes:
        return True, f"ALERT! Free disk space: {round(free/DigitalInfoEnum.gb, 1)} gb is less than the threshold: {round(free_bytes/DigitalInfoEnum.gb, 1)} gb"
    else:
        return False, f"Free disk space: {round(free/DigitalInfoEnum.gb, 1)} gb is more than the threshold: {round(free_bytes/DigitalInfoEnum.gb, 1)} gb"
