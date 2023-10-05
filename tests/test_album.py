from lib.album import Album


def test_artist_constructs():
    album = Album(1, "Test Album", 1990, 1)
    assert album.id == 1
    assert album.title == "Test Album"
    assert album.release_year == 1990
    assert album.artist_id == 1

