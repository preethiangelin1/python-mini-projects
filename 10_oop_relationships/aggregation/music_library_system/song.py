class Song:
    def __init__(self, title, artist, duration):
        self._title = title
        self._artist = artist
        self._duration = duration

    @property
    def title(self):
        return self._title

    @property
    def artist(self):
        return self._artist

    @property
    def duration(self):
        return self._duration