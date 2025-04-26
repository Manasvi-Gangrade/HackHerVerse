import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DB_PATH = os.getenv('DB_PATH', 'neuroease.db')   # Default database path
    MQTT_BROKER = os.getenv('MQTT_BROKER', 'localhost')
    MQTT_PORT = os.getenv('MQTT_PORT', 1883)
    LOGGING_LEVEL = os.getenv('LOGGING_LEVEL', 'DEBUG')
