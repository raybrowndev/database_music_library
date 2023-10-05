from lib.album import Album

class AlbumRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute(
            """SELECT * 
        FROM albums""")
        album_list = []
        for row in rows:
            item = Album(row["id"],row['title'], row['release_year'], row['artist_id'])
            album_list.append(item)
        return album_list 
    
    def find(self, album_id):
        rows = self._connection.execute('SELECT * from album WHERE id = %s', [album_id])
        i = rows[0]
        return Album(i["id"],i['title'], i['release_year'], i['artist_id'])
        
    def create(self, new_album):
        self._connection.execute('INSERT INTO albums (title, release_year, artist_id) VALUES (%s, %s, %s)',[new_album.title, new_album.release_year, new_album.artist_id])
        return None

    def delete(self, del_id):
        self._connection.execute('DELETE FROM albums WHERE id = %s', [del_id])
        return None 
    
    def all_with_names(self):
        rows = self._connection.execute(
            """SELECT albums.id, albums.title, albums.artist_id, artists.name 
            FROM albums JOIN artists 
            ON artists.id = albums.artist_id""")
        album_list = []
        for row in rows:
            item = Album(row["id"],row['title'], row['artist_id'], row['name'])
            album_list.append(item)
        return album_list 
