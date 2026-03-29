from playlist import Playlist
class User:
    def __init__(self, name):
        self._name = name
        self._playlists = []

    @property
    def name(self):
        return self._name

    @property
    def playlists(self):
        return list(self._playlists)  # safe copy

    def create_playlist(self, name):
        playlist = Playlist(name)
        self._playlists.append(playlist)
        return playlist

    def delete_playlist(self, playlist):
        if playlist in self._playlists:
            self._playlists.remove(playlist)