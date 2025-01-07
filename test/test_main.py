from unittest.mock import patch, mock_open
from main import (parse_spotify_songs, get_songs_by_artist, get_songs_by_year,
                         sort_artists_by_number_of_songs, get_songs_above_given_streams)

def test_parse_spotify_songs_file_not_found():
    with patch("os.path.exists", return_value=False):
        result = parse_spotify_songs("nonexistent.csv")
        assert result == []

def test_parse_spotify_songs_valid_file():
    mock_data = "Artist,Release Date,Spotify Streams\nArtist1,01/01/2022,1,000,000\n"
    with patch("os.path.exists", return_value=True):
        with patch("builtins.open", mock_open(read_data=mock_data)):
            result = parse_spotify_songs("mock_file.csv")
            assert len(result) == 1
            assert result[0]['Artist'] == "Artist1"

def test_get_songs_by_artist():
    songs = [
        {"Artist": "Artist1", "Release Date": "01/01/2022", "Spotify Streams": "1,000,000"},
        {"Artist": "Artist2", "Release Date": "01/01/2021", "Spotify Streams": "500,000"}
    ]
    result = get_songs_by_artist(songs, "Artist1")
    assert len(result) == 1
    assert result[0]['Artist'] == "Artist1"

def test_get_songs_by_year():
    songs = [
        {"Artist": "Artist1", "Release Date": "01/01/2022", "Spotify Streams": "1,000,000"},
        {"Artist": "Artist2", "Release Date": "01/01/2021", "Spotify Streams": "500,000"}
    ]
    result = get_songs_by_year(songs, 2022)
    assert len(result) == 1
    assert result[0]['Release Date'] == "01/01/2022"

def test_sort_artists_by_number_of_songs():
    songs = [
        {"Artist": "Artist1", "Release Date": "01/01/2022", "Spotify Streams": "1,000,000"},
        {"Artist": "Artist2", "Release Date": "01/01/2021", "Spotify Streams": "500,000"},
        {"Artist": "Artist1", "Release Date": "01/01/2021", "Spotify Streams": "2,000,000"}
    ]
    result = sort_artists_by_number_of_songs(songs)
    assert result == {"Artist1": 2, "Artist2": 1}

def test_get_songs_above_given_streams():
    songs = [
        {"Artist": "Artist1", "Release Date": "01/01/2022", "Spotify Streams": "1,000,000,000"},
        {"Artist": "Artist2", "Release Date": "01/01/2021", "Spotify Streams": "500,000,000"},
        {"Artist": "Artist1", "Release Date": "01/01/2021", "Spotify Streams": "2,000,000,000"}
    ]
    result = get_songs_above_given_streams(songs, 1000000000)
    assert len(result) == 2
    assert result[0]['Spotify Streams'] == "1,000,000,000"
