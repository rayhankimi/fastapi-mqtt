from pydantic import BaseModel
from datetime import datetime


class MQTTModel(BaseModel):
    topic: str
    payload: str
    timestamp: datetime
