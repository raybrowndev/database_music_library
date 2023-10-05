from lib.album import Album
from lib.album_repository import AlbumRepository

def test_create_record(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)

    repository.create(Album(None, "Album title", 1990, 2))
    result = repository.all()
    assert result == [
        Album(1, 'Doolittle', 1989, 1),
        Album(2, 'Album title', 1990, 2)
    ]


def test_delete_album(db_connection):
    db_connection.seed('seeds/music_library.sql')
    repo = AlbumRepository(db_connection)

    repo.create(Album(2, "Best Album", 2023, 1))
    repo.delete(2)
    result = repo.all()
    assert result == [
        Album(1, 'Doolittle', 1989, 1)
    ]
    
