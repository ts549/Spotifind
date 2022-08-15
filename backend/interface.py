import chunk
from voice_recorder import Recorder
from speech_converter import Recognizer
from nlp.nltkAnalysis import NltkAnalyzer
from Spotify_API.spotify_api import SpotifyAPI

class Interface:

    def record(self, time):
        recorder = Recorder(chunk=1024, channels=1, rate=44100)
        recorder.record(time=time)


    def convert(self, audio_file):
        recognizer = Recognizer()
        text = recognizer.convert(audio_file)
        return text

    def emotion_analysis(self, text):
        analyzer = NltkAnalyzer()
        emotions = analyzer.emotion_analysis(text)
        return emotions

    def sentiment_analysis(self, text):
        analyzer = NltkAnalyzer()
        sentiment = analyzer.sentiment_analysis(text)
        return sentiment

    def generate_playlist(self, mood):
        spotifyAPI = SpotifyAPI()
        print ("LINE 31")
        print(mood)
        playlist = spotifyAPI.generatePlaylists(mood)
        return playlist

    def get_top3_songs(self, mood):
        spotifyAPI = SpotifyAPI()
        top3 = spotifyAPI.get_top3_songs(mood)
        return top3

