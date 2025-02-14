from typing import List
import paho.mqtt.client as mqtt

from app.models.ThingsModel import MQTTConfig


def setup_mqtt_connection(config: MQTTConfig) -> mqtt.Client:
    client = mqtt.Client()
    client.username_pw_set(config.mqtt_username, config.mqtt_password)
    client.on_connect = lambda client, userdata, flags, rc: on_connect(client, userdata, flags, rc, config)
    client.on_message = lambda client, userdata, message: on_message(client, userdata, message)
    client.connect(config.mqtt_broker, config.mqtt_port)
    return client


def on_connect(client: mqtt.Client, userdata: dict, flags: dict, rc: int, config: MQTTConfig) -> None:
    print(f"Connected to MQTT with result code {rc}")
    topics = [f"{config.mqtt_topic}{i}" for i in range(1, config.num_devices + 1)]
    for topic in topics:
        client.subscribe(topic)
        print(f"Subscribed to topic '{topic}'")


def on_message(client: mqtt.Client, userdata: dict, message: mqtt.MQTTMessage) -> None:
    print(f"Received message '{message.payload.decode()}' on topic '{message.topic}'")
