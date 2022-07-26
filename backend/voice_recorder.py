import pyaudio
import wave

class Recorder:

    def __init__(self, chunk, channels, rate):
        self.CHUNK = chunk
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = channels
        self.RATE = rate
        self.recorder = pyaudio.PyAudio()
        self.OUTPUT_WAV = "output.wav"

    def record(self, time):
        stream = self.recorder.open(
            format = self.FORMAT,
            channels = self.CHANNELS,
            rate = self.RATE,
            input = True,
            input_device_index=1,
            frames_per_buffer = self.CHUNK
        )

        print("start recording...")

        frames = []
        for i in range(0, int(self.RATE / self.CHUNK * time)):
            data = stream.read(self.CHUNK)
            frames.append(data)

        print("recording stopped...")

        stream.stop_stream()
        stream.close()
        self.recorder.terminate()

        wf = wave.open(self.OUTPUT_WAV, "wb")
        wf.setnchannels(self.CHANNELS)
        wf.setsampwidth(self.recorder.get_sample_size(self.FORMAT))
        wf.setframerate(self.RATE)
        wf.writeframes(b''.join(frames))
        wf.close()