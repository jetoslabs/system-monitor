from pydantic import BaseModel


class AlertSchema(BaseModel):
    is_alert: bool


class DiskSpaceSchema(AlertSchema):
    total: float
    used: float
    free: float


class VitalsSchema(BaseModel):
    diskspace: DiskSpaceSchema

