import shutil
from typing import Tuple


def get_disk_usage(path: str) -> Tuple[int, int, int]:
    stat = shutil.disk_usage(path)
    return stat


def alert_for_disk_usage(stat: Tuple[int, int, int], *, free_bytes: int) -> (bool, str):
    free = stat[2]
    if free > free_bytes:
        return free > free_bytes, f"Free disk space: {free} bytes is less than the threshold: {free_bytes} bytes"
    return False, ""
