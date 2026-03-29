class Playlist:
    def __init__(self, name):
        self._name = name
        self._songs = []

    @property
    def name(self):
        return self._name

    @property
    def songs(self):
        return list(self._songs)

    def add_song(self, song):
        if song not in self._songs:
            self._songs.append(song)

    def remove_song(self, song):
        if song in self._songs:
            self._songs.remove(song)

    @property
    def song_count(self):
        return len(self._songs)

    @property
    def total_duration(self):
        return sum(song.duration for song in self._songs)