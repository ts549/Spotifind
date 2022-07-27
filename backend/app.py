from flask import Flask, request, jsonify, send_from_directory
from interface import Interface

app = Flask(__name__)

interface = Interface()

@app.route("/test", methods = ["GET"])
def test():
    return {'test' : 'string'}

@app.route("/", defaults={'path':''})
def index():
    return send_from_directory('../frontend/src','index.html')

@app.route("/icons/spotify-logo.png", methods = ["GET"])
def spotify_logo():
    return send_from_directory('../frontend/icons', 'spotify-logo.png')

@app.route("/icons/menu.png", methods = ["GET"])
def menu():
    return send_from_directory('../frontend/icons', 'menu.png')

@app.route("/icons/audio.gif", methods = ["GET"])
def audio_gif():
    return send_from_directory('../frontend/icons', 'audio.gif')

@app.route("/icons/play.png", methods= ["GET"])
def play():
    return send_from_directory('../frontend/icons', 'play.png')

@app.route("/api/start_record", methods = ["POST"])
def start_record():
    data = request.get_json()
    print(data['time'])
    interface.record(time=int(data['time']))
    text = interface.convert('output.wav')
    
    if (text is not None):
        return {'response' : '200',
                'translation' : text}

if __name__ == "__main__":
    app.run(debug=True)