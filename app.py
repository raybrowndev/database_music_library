# from lib.database_connection import DatabaseConnection
# from lib.artist_repository import ArtistRepository


# # Connect to the database
# connection = DatabaseConnection()
# connection.connect()

# # Seed with some seed data
# connection.seed("seeds/music_library.sql")

# # Retrieve all artists
# artist_repository = ArtistRepository(connection)
# artists = artist_repository.all()

# # List them out
# for artist in artists:
#     print(artist)


from lib.artist import Artist
from lib.album import  Album
from lib.artist_repository import ArtistRepository
from lib.album_repository import AlbumRepository
from lib.database_connection import DatabaseConnection

class Application():
    def __init__(self):
        self._connection = DatabaseConnection()
        self._connection.connect()
        self._connection.seed("seeds/music_library.sql")

    def run(self):
        prompt = f"Welcome to the music library manager!\n\nWhat would you like to do?\n\n1 - List all artists\n2 - List all albums\n3 - List all artists + albums"
        print(prompt)
        answer = int(input("Enter your choice:"))

        if answer == 1:
            artist_repository = ArtistRepository(self._connection)
            all_artists = artist_repository.all()
            for i in all_artists:
                print(f"{i.id}: {i.name} ({i.genre})")
        elif answer == 2:
            album_repository = AlbumRepository(self._connection)
            all_albums = album_repository.all()
            for album in all_albums:
                print(f"{album.id}: {album.title} ({album.release_year}) by {album.artist_id}")
        elif answer == 3:
            artist_repository = ArtistRepository(self._connection)
            album_repository = AlbumRepository(self._connection)

            all_artists = artist_repository.all()
            all_albums = album_repository.all()

            print(f"\n------Artist------\n")
            for artist in all_artists:
                print(f"{artist.id}: {artist.name} ({artist.genre})")
            
            print(f"\n------Albums------\n")
            for album in all_albums:
                print(f"{album.id}: {album.title} ({album.release_year}) {album.artist_id}")
        else:
            return f"No option has been chosen"

    def add_one_artist(self, new_artist):
            repo = ArtistRepository(self._connection)
            repo.create(new_artist)

    def add_one_album(self, new_album):
            repo = AlbumRepository(self._connection)
            repo.create(new_album)
    
    def full_list(self):
        album_repo = AlbumRepository(self._connection)
        all_albums = album_repo.all_with_names()
        for album in all_albums:
                print(f"{album.id}: {album.title} by {album.artist_id}")

        
        

if __name__ == '__main__': #run if direct, not importing
    app = Application()
    app.add_one_artist(Artist(None, "Billie Eilish", "Alternative"))
    app.add_one_artist(Artist(None, "SZA", "RnB"))
    app.add_one_album(Album(None, "Happier Than Ever", 2021, 5,))
    app.run()

    app.full_list()
