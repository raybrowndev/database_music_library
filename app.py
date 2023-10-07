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

    def list_artist(self):
        artist_repository = ArtistRepository(self._connection)
        all_artists = artist_repository.all()
        title = "1 - List all artists"
        print(f"\n------{title.upper()}------\n")
        for i in all_artists:
            print(f"{i.id}: {i.name} ({i.genre})")
            
    
    def list_albums(self):
        album_repository = AlbumRepository(self._connection)
        all_albums = album_repository.all_with_names()
        title = "1 - List all albums"
        print(f"\n------{title.upper()}------\n")
        for album in all_albums:
            print(f"{album.id}: {album.title} by {album.artist_id}")

    def list_art_and_al(self):
        artist_repository = ArtistRepository(self._connection)
        album_repository = AlbumRepository(self._connection)

        all_artists = artist_repository.all()
        all_albums = album_repository.all_with_names()
        title = "3 - List all artists + albums"
        print(f"\n------{title.upper()}------\n")
        print(f"\n------Artist------\n")
        for artist in all_artists:
            print(f"{artist.id}: {artist.name} ({artist.genre})")
        
        print(f"\n------Albums------\n")
        for album in all_albums:
            print(f"{album.id}: {album.title} by {album.artist_id}")

    def run(self):
        prompt =(
            f"Welcome to the music library manager!\n\n"
            f"What would you like to do?\n\n"
            f"1 - List all artists\n"
            f"2 - List all albums\n"
            f"3 - List all artists + albums")
        print(prompt)
        answer = int(input("Enter your choice:"))
        
        if answer == 1:
            self.list_artist()
        elif answer == 2:
            self.list_albums()
        elif answer == 3:
            self.list_art_and_al()
        else: 
            print("Invalid option! Enter 1, 2 or 3")

    def add_one_artist(self, new_artist):
            repo = ArtistRepository(self._connection)
            repo.create(new_artist)

    def add_one_album(self, new_album):
            repo = AlbumRepository(self._connection)
            repo.create(new_album)    
        

if __name__ == '__main__': #run if direct, not importing
    app = Application()
    app.add_one_artist(Artist(None, "Billie Eilish", "Alternative"))
    app.add_one_artist(Artist(None, "SZA", "RnB"))
    app.add_one_album(Album(None, "Happier Than Ever", 2021, 5,))
    app.run()
    

    # app.full_list()
