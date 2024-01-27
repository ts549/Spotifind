from ast import For
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# scope = "user-library-read user-top-read"
# sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

class SpotifyAPI:
    def authorize(self):
        SPOTIPY_CLIENT_ID='37b1ec59796f4d068a9cc098be57bc75'
        SPOTIPY_CLIENT_SECRET='8834c64cabea4fe6af7bd03aa1af22c5'
        SPOTIPY_REDIRECT_URI='https://www.google.com/'
        SCOPE="user-library-read user-top-read playlist-modify-public"
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri=SPOTIPY_REDIRECT_URI, scope=SCOPE))
        return sp

    def generatePlaylists(self, mood):
        mood = (mood + 1) / 2
        sp = self.authorize()
        top_songs = sp.current_user_top_tracks(limit=50, time_range='medium_term')['items']
        playlist = []
        uris = []
        for song in top_songs:
            uri = song['uri']
            audio_features = sp.audio_features(uri)
            for feature in audio_features:
                if mood < 0.10:
                    if (feature['valence'] < mood):
                        playlist.append([song['name'], uri])
                        uris.append(uri)
                elif 0.10 <= mood < 0.20:
                    if (0.1 <= feature['valence'] < 0.2):
                        playlist.append([song['name'], uri])
                        uris.append(uri)
                elif 0.25 <= mood < 0.50:
                    if (0.25 <= feature['valence'] < 0.5):
                        playlist.append([song['name'], uri])
                        uris.append(uri)
                elif 0.50 <= mood < 0.75:
                    if (0.5 <= feature['valence'] < 0.75):
                        playlist.append([song['name'], uri])
                        uris.append(uri)
                elif 0.75 <= mood < 0.90:
                    if (0.75 <= feature['valence'] < 0.9):
                        playlist.append([song['name'], uri])
                        uris.append(uri)
                elif mood >= 0.90:
                    if (0.9 <= feature['valence'] <= 1):
                        playlist.append([song['name'], uri])
                        uris.append(uri)


        # print(playlist)
        print(sp.current_user()['id'])
        playlist_id = sp.user_playlist_create(sp.current_user()['id'], name="The Mood Colon: " + str(mood), public=True, description="")['id']

        print(playlist_id)
        sp.playlist_add_items(playlist_id, uris, position=None)

  
        return playlist_id

    def get_top3_songs(self, mood): 
        sp = self.authorize()
        playlist_id = self.generatePlaylists(mood)
        songs = sp.playlist_items(playlist_id, fields=None, limit=3, offset=0, market=None, additional_types=('track', 'episode'))['items']
        top3 = []
        for song in songs:
            top3.append(song['track']['name'])
        print("top 3 songs:")
        print(top3)
        return top3
        


# 1) get current playing song in spotify api
# 2) add to interface
# 3) add route to app.py
# 4) get info from backend url to frontend 
# 5) display current playing song in correct format
