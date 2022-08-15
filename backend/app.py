from flask import Flask, request, jsonify, send_from_directory
from interface import Interface
from flask_cors import CORS

# Starts Flask connection
app = Flask(__name__)
CORS(app)
interface = Interface()

# Routing paths ---
# Sets up a proxy for all frontend requests from port 3000 to port 5000


@app.route("/", defaults={'path': ''})
def index():
    return send_from_directory('../frontend/src', 'index.html')


@app.route("/icons/spotify-logo.png", methods=["GET"])
def spotify_logo():
    return send_from_directory('../frontend/icons', 'spotify-logo.png')


@app.route("/icons/menu.png", methods=["GET"])
def menu():
    return send_from_directory('../frontend/icons', 'menu.png')


@app.route("/icons/audio.gif", methods=["GET"])
def audio_gif():
    return send_from_directory('../frontend/icons', 'audio.gif')


@app.route("/icons/play.png", methods=["GET"])
def play():
    return send_from_directory('../frontend/icons', 'play.png')


@app.route("/test", methods=["GET"])
def test():
    print("IN TEST ROUTE")
    return {'test': 'tao likes kids'}


@app.route("/api/start_record", methods=["POST"])
def start_record():
    data = request.get_json()
    print(data['time'])
    interface.record(time=int(data['time']))
    text = interface.convert('output.wav')

    if (text is not None):
        emotion = interface.emotion_analysis(text)
        sentiment = interface.sentiment_analysis(text)
        mood = sentiment['compound']
        print("MOOD DISOCVERD: ")
        print(mood)
        playlist = interface.generate_playlist(mood)
        top3 = interface.get_top3_songs(mood)
        return {'response': '200',
                'text': text,
                'emotion': emotion,
                'sentiment': sentiment,
                'playlist generated': playlist,
                'top 3 songs': top3}


if __name__ == "__main__":
    app.run(debug=True)
