import pyaudio
import wave

class Recorder:

    def __init__(self, chunk, format, channels, rate):
        self.CHUNK = chunk
        self.FORMAT = format
        self.CHANNELS = channels
        self.RATE = rate
        self.recorder = pyaudio.PyAudio()

    def record(self, seconds):
        stream = self.recorder.open(
            format = self.FORMAT,
            channels = self.CHANNELS,
            rate = self.RATE,
            input = True,
            frames_per_buffer = self.CHUNK
        )

        print("start recording...")

        frames = []
        for i in range(0, int(self.RATE / self.CHUNK * seconds)):
            data = stream.read(self.CHUNK)
            frames.append(data)

        print("recording stopped...")

        stream.stop_stream()
        stream.close()
        self.recorder.terminate()