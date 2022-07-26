import chunk
from voice_recorder import Recorder
from speech_converter import Recognizer

class Interface:

    def record(self, time):
        recorder = Recorder(chunk=1024, channels=1, rate=44100)
        recorder.record(time=time)
    
    def convert(self, audio_file):
        recognizer = Recognizer()
        text = recognizer.convert(audio_file)
        return text