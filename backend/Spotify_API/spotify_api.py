from ast import For
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# scope = "user-library-read user-top-read"
# sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

class SpotifyAPI:
    def generatePlaylists(self, mood):
        SPOTIPY_CLIENT_ID='e89e725228ac43bfba56a3a785b8930f'
        SPOTIPY_CLIENT_SECRET='73763bff46934dafb4075cd9f4bc021f'
        SPOTIPY_REDIRECT_URI='https://www.google.com/'
        SCOPE="user-library-read user-top-read playlist-modify-public"
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri=SPOTIPY_REDIRECT_URI, scope=SCOPE))

        print ("FUCK YOU")
        top_songs = sp.current_user_top_tracks(limit=20, time_range='medium_term')['items']

        mood = 0.9
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
        playlist_id = sp.user_playlist_create(sp.current_user()['id'], name="The Mood Colon: " + str(mood), public=True, description="sopweepwee")['id']

        print(playlist_id)
        sp.playlist_add_items(playlist_id, uris, position=None)

        return playlist_id



# mood = 0.8
# playlist = []
# for song in top_songs:
#     uri = song['uri']
#     audio_features = sp.audio_features(uri)
#     for feature in audio_features:
#         if mood < 0.10:
#             if (feature['valence'] <= (mood + 0.1)
#                 and feature['danceability'] <= (mood * 8)
#                 and feature['energy'] <= (mood * 10)):
#                     playlist.append([song['name'], uri])
#         elif 0.10 <= mood < 0.20:
#             if ((mood-0.075) <= feature['valence'] <= (mood+0.075) 
#                 and feature['danceability'] >= (mood*4)
#                 and feature['energy'] >= (mood*5)):
#                     playlist.append([song['name'], uri])
#         elif 0.25 <= mood < 0.50:
#             if ((mood-0.05) <= feature['valence'] <= (mood + 0.05)
#                 and feature['danceability'] <= (mood * 1.75)
#                 and feature['energy'] >= (mood * 1.75)):
#                     playlist.append([song['name'], uri])
#         elif 0.50 <= mood < 0.75:
#             if ((mood-0.075) <= feature['valence'] <= (mood+0.075)
#                 and feature['danceability'] >= (mood/2.5)
#                 and feature['energy'] >= (mood / 2)):
#                     playlist.append([song['name'], uri])
#         elif 0.75 <= mood < 0.90:
#             if ((mood-0.075) <= feature['valence'] <= (mood+0.075) 
#                 and feature['danceability'] >= (mood/2)
#                 and feature['energy'] >= (mood *1.75)):
#                     playlist.append([song['name'], uri])
#         elif mood >= 0.90:
#             if ((mood-0.15) <= feature['valence'] <= 1
#                 and feature['danceability'] >= (mood/1.75)
#                 and feature['energy'] >= (mood *1.5)):
#                     playlist.append([song['name'], uri])
