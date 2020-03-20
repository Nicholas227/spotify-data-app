
# Returns a list of the user's top 10 artists
def get_top_artists(data):
    artists = []
    items = data['items']
    for item in items:
        artist_name = item['id']
        artists.append(artist_name)
    return artists

# Returns a list of the user's top 10 tracks
def get_top_tracks(data):
    tracks = {}
    for item in data['items']:
        track_name = item['id']
        artist_name = item['artists'][0]['id']
        tracks[track_name] = artist_name
    return tracks

# Returns a python dictionary with the top 50 tracks grouped by the artist
def get_top_tracks_by_artist(top_tracks, top_artists):
    top_tracks_by_artist = {}
    for artist in top_artists:
        tracks = []
        for track in top_tracks:
            track_artist = top_tracks.get(track)
            if artist == track_artist:
                tracks.append(track)
        if len(tracks) > 0:
        	top_tracks_by_artist[artist] = tracks
    return top_tracks_by_artist