from pydantic import BaseModel
from datetime import datetime


class MQTTConfig(BaseModel):
    num_devices: int
    mqtt_broker: str
    mqtt_port: int
    mqtt_topic: str
    mqtt_username: str
    mqtt_password: str
