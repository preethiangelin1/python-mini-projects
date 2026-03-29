from user import User
from artist import Artist
from song import Song
from library import Library


if __name__ == "__main__":

    user = User("John")
    playlist = user.create_playlist("Workout")

    artist1 = Artist("Coldplay")
    artist2 = Artist("Adele")

    song1 = Song("Yellow", artist1, 269)
    song2 = Song("Clocks", artist1, 307)
    song3 = Song("Hello", artist2, 296)

    library = Library()
    library.add_song(song1)
    library.add_song(song2)
    library.add_song(song3)

    playlist.add_song(song1)
    playlist.add_song(song2)
    playlist.add_song(song3)
    playlist.add_song(song1)

    print(f"Library has {library.song_count} songs")
    print(f"{playlist.name} ({playlist.song_count} songs, {playlist.total_duration}s)")

    for s in playlist.songs:
        print(f"  - {s.title} by {s.artist.name} ({s.duration}s)")