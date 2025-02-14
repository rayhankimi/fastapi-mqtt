import paho.mqtt.client as mqtt
import asyncio
import os

from datetime import datetime

from dotenv import load_dotenv

from app.models.ThingsModel import MQTTConfig
from app.services.Things.ThingsController import setup_mqtt_connection

load_dotenv()

config = MQTTConfig(
    mqtt_broker="mosquitto",
    mqtt_port=1883,
    mqtt_topic="device/",
    num_devices=3,
    mqtt_username=os.environ.get("MOSQUITTO_USERNAME", "default_user"),
    mqtt_password=os.environ.get("MOSQUITTO_PASSWORD", "default_password")
)


class MQTTConnection:
    def __init__(self):
        self.client = None

    def start_connection(self):
        self.client = setup_mqtt_connection(config)
        self.client.loop_start()


mqtt_connection = MQTTConnection()
