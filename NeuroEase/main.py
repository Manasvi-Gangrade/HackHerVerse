from flask import Flask, jsonify
from voice_control.voice_commands import VoiceControl
from emotion_detector.emotion_model import EmotionModel
from gesture_control.gesture_recognition import GestureRecognition
from db_handler.database import create_db, save_task, get_tasks
from iot_integration.mqtt_handler import MQTTHandler
import logging

app = Flask(__name__)
voice_control = VoiceControl()
emotion_model = EmotionModel()
gesture_recognition = GestureRecognition()
mqtt_handler = MQTTHandler()

logger = logging.getLogger("NeuroEase")

@app.route('/')
def home():
    return jsonify({"message": "NeuroEase Server is Running!"})

@app.route('/get_tasks')
def fetch_tasks():
    tasks = get_tasks()
    return jsonify({"tasks": tasks})

@app.route('/voice_command', methods=['POST'])
def voice_command():
    command = voice_control.listen_for_commands()
    logger.info(f"Received command: {command}")
    return jsonify({"command": command})

if __name__ == "__main__":
    create_db()
    app.run(debug=True)
