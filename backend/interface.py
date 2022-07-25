import chunk
from voice_recorder import Recorder

class Interface:

    def record(self, time):
        recorder = Recorder(chunk=1024, channels=1, rate=44100)
        recorder.record(time=time)