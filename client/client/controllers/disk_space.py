import shutil
from typing import Tuple
from loguru import logger

from client.clients.nats import send_vitals
from client.controllers.twitter import Twitter
from client.core.constants import DigitalInfoEnum
from client.schemas.schema_twitter import TweetReqSchema
from client.schemas.schema_vitals import DiskSpaceSchema, VitalsSchema


async def run():
    logger.bind().debug("disk usage...")
    diskspace: DiskSpaceSchema = alert_for_disk_usage("/", free_bytes=50*DigitalInfoEnum.gb)

    vitals = VitalsSchema(
        diskspace=diskspace
    )
    logger.bind(vitals=vitals).debug(f"vitals")

    if vitals and vitals.diskspace and vitals.diskspace.is_alert:
        # # send vitals to NATS topic vitals, on alert
        # await send_vitals(vitals)

        tweet_req = TweetReqSchema(text=f"Alert: Free space is now {round(vitals.diskspace.free/DigitalInfoEnum.gb, 1)} gb")
        # send tweet
        tweet_res = Twitter.create_tweet(tweet_req)
        logger.bind(tweet_req=tweet_req, tweet_res=tweet_res).info("Tweeted")


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
