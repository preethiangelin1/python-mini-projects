class Library:
    def __init__(self):
        self._songs = []

    @property
    def songs(self):
        return list(self._songs)

    def add_song(self, song):
        if song not in self._songs:
            self._songs.append(song)

    @property
    def song_count(self):
        return len(self._songs)