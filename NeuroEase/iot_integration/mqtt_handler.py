import paho.mqtt.client as mqtt
from config.config import Config

class MQTTHandler:
    def __init__(self):
        self.client = mqtt.Client()
        self.client.connect(Config.MQTT_BROKER, Config.MQTT_PORT)

    def publish(self, topic, message):
        self.client.publish(topic, message)
