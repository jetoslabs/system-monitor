import shutil
from typing import Tuple
from loguru import logger


def run():
    logger.bind().debug("disk usage...")
    is_alert, alert_msg = alert_for_disk_usage("/", free_bytes=20182291968)
    logger.bind(is_alert=is_alert, alert_msg=alert_msg).debug(f"ALERT! - disk usage")


def get_disk_usage(path: str) -> Tuple[int, int, int]:
    stat = shutil.disk_usage(path)
    logger.bind(stat=stat).debug(f"get_disk_usage")
    return stat


def alert_for_disk_usage(path: str, free_bytes: int) -> (bool, str):
    total, used, free = get_disk_usage(path)
    if free < free_bytes:
        return True, f"Free disk space: {free} bytes is less than the threshold: {free_bytes} bytes"
    return False, ""
