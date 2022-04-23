import nats
from loguru import logger

from client.core.settings import settings
from client.schemas.schema_vitals import VitalsSchema


async def send_vitals(vitals: VitalsSchema):
    try:
        nc = await nats.connect(settings.NATS_URI)
        vitals_json = vitals.json()
        vitals_bytes = str.encode(vitals_json)
        await nc.publish(settings.NATS_TOPIC_VITALS, vitals_bytes)
        logger.bind(
            nats_uri=settings.NATS_URI, topic=settings.NATS_TOPIC_VITALS, msg=vitals.json()
        ).info("Published message")
    finally:
        pass

