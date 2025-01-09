import csv
import os
from flask import Flask, jsonify

app = Flask(__name__)

YEAR_OFFSET = -4
PORT = 8080
IP_ADDRESS = '127.0.0.1'


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
    for song in songs:
        if int(song['Release Date'][YEAR_OFFSET:]) == year:
            songsByYear.append(song)
            print(song)
    return songsByYear

def sort_artists_by_number_of_songs(songs):
    artists = {}
    for song in songs:
        if song['Artist'] in artists:
            artists[song['Artist']] += 1
        else:
            artists[song['Artist']] = 1
    return dict(sorted(artists.items(), key=lambda item: item[1], reverse=True))

def get_songs_above_given_streams(songs, streams):
    billionsSongs = []
    for song in songs:
        songCopy = song['Spotify Streams'].replace(',', '')
        if  songCopy.isdigit() and int(songCopy) >= streams:
            billionsSongs.append(song)
    return billionsSongs

@app.route('/songs/above/<int:streams>', methods=['GET'])
def get_songs(streams):
    filePath = "data.csv"  
    songsResult = parse_spotify_songs(filePath)
    result = get_songs_above_given_streams(songsResult, streams)
    return jsonify(result) 

if __name__ == "__main__":
    app.run(host=IP_ADDRESS, port=PORT)
