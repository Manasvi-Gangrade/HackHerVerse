from flask import Flask, jsonify
from voice_control.voice_commands import VoiceControl
from emotion_detector.emotion_model import EmotionModel
from gesture_control.gesture_recognition import GestureRecognition
from db_handler.database import create_db, save_task, get_tasks
from iot_integration.mqtt_handler import MQTTHandler
import logging

app = Flask(__name__)

# Initialize components
voice_control = VoiceControl()
emotion_model = EmotionModel()
gesture_recognition = GestureRecognition()
mqtt_handler = MQTTHandler()

# Setup logger
logger = logging.getLogger("NeuroEase")

# Routes
@app.route('/')
def home():
    return jsonify({"message": "NeuroEase Server is Running!"})

@app.route('/get_tasks', methods=['GET'])
def fetch_tasks():
    tasks = get_tasks()
    return jsonify({"tasks": tasks})

@app.route('/voice_command', methods=['POST'])
def voice_command():
    command = voice_control.listen_for_commands()
    logger.info(f"Received command: {command}")
    return jsonify({"command": command})

@app.route('/save_task', methods=['POST'])
def save_user_task():
    # Assuming you have data like task and mood from the request
    task = "Sample Task"
    mood = "Happy"
    save_task(task, mood)
    return jsonify({"message": "Task saved successfully!"})

@app.route('/mqtt_message', methods=['POST'])
def send_mqtt_message():
    message = "Sample message to MQTT"
    mqtt_handler.publish("test/topic", message)
    return jsonify({"message": "MQTT message sent successfully!"})

if __name__ == "__main__":
    create_db()  # Ensure DB is created
    app.run(debug=True, host='0.0.0.0', port=5000)  # Start the Flask app on port 5000
