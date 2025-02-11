import paho.mqtt.client as mqtt
import asyncio
import os

from datetime import datetime

from dotenv import load_dotenv

load_dotenv()

DEVICE_ID = 1
MQTT_BROKER = "mosquitto"
MQTT_PORT = 1883
MQTT_TOPIC = "device/" + str(DEVICE_ID)
MQTT_USERNAME = os.environ.get("MOSQUITTO_USERNAME")
MQTT_PASSWORD = os.environ.get("MOSQUITTO_PASSWORD")


def on_connect(client, userdata, flags, rc):
    print(f"Connected to MQTT with result code {rc}")
    client.subscribe(MQTT_TOPIC)


def on_message(client, userdata, message):
    print(f"Received message '{message.payload.decode()}' on topic '{message.topic}'")
    print(f"Message timestamp: {datetime.now()}")


class MQTTConnection:
    def __init__(self):
        self.client = None

    def start_connection(self):
        self.client = mqtt.Client()
        self.client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)
        self.client.on_connect = on_connect
        self.client.on_message = on_message
        self.client.connect(MQTT_BROKER, MQTT_PORT)
        self.client.loop_start()


mqtt_connection = MQTTConnection()