import csv
import os

BILLION = 1000000000
YEAR_OFFSET = -4

def parse_spotify_songs(filePath):
    songs = []
    if not os.path.exists(filePath):
        print(f"Error: The file {filePath} does not exist.")
        return songs

    try:
        with open(filePath, mode='r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                songs.append(row)
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")

    return songs

def get_songs_by_artist(songs, artist):
    songsByArtist = []
    for song in songs:
        if song['Artist'] == artist:
            songsByArtist.append(song)
    return songsByArtist

def get_songs_by_year(songs, year):
    songsByYear = []
    print(year)
    for song in songs:
        if int(song['Release Date'][YEAR_OFFSET:]) == year:
            songsByYear.append(song)
    return songsByYear

def get_billions_songs(songs):
    billionsSongs = []
    for song in songs:
        songCopy = song['Spotify Streams'].replace(',', '')
        if  songCopy.isdigit() and int(songCopy) >= BILLION:
            billionsSongs.append(song)
    return billionsSongs

if __name__ == "__main__":
    filePath = "data.csv"
    songsResult = parse_spotify_songs(filePath)
    print(get_songs_by_artist(songsResult, "The Weeknd"))
    print(get_songs_by_year(songsResult, 2022))
    print(get_billions_songs(songsResult))
