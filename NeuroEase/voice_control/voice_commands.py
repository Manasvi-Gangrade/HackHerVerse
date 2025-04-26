import speech_recognition as sr
import pyttsx3

class VoiceControl:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()

    def listen_for_commands(self):
        with sr.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source)
            print("Listening for commands...")
            audio = self.recognizer.listen(source)
            return self.recognizer.recognize_google(audio)

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()
