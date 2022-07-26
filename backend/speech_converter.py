import speech_recognition as sr

class Recognizer:

    def __init__(self):
        self.recognizer = sr.Recognizer()

    def convert(self, audio_file):
        with sr.AudioFile(audio_file) as source:
            # listen for the data (load audio to memory)
            audio_data = self.recognizer.record(source)
            # recognize (convert from speech to text)
            text = self.recognizer.recognize_google(audio_data)

            return text