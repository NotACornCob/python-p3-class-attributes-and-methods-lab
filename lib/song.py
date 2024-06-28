import ipdb

class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}
    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.count += 1
        Song.genres.append(genre)
        Song.artists.append(artist)
        Song.add_to_genre_count(genre) 
        Song.add_to_artist_count(artist)
    
    def add_song_to_count():
            count = count+1
    
    @classmethod
    def add_to_genres(cls,genre):
        unique_genres = [genre]
        for song_genre in cls.genres:
            if song_genre not in unique_genres:
                unique_genres.append(song_genre)
        cls.genres = unique_genres
                    
    @classmethod
    def add_to_genre_count(cls, genre):
        cls.genre_count[genre] = cls.genre_count.get(genre, 0) + 1

    @classmethod 
    def add_to_artists(cls,artist):
        unique_artists = [artist]
        for song_artist in cls.artists:
            if song_artist not in unique_artists:
                unique_artists.append(song_artist)
            cls.artists = unique_artists

    @classmethod
    def add_to_artist_count(cls, artist):
        cls.artist_count[artist] = cls.artist_count.get(artist, 0) + 1


ninety_nine_problems = Song("99 Problems", "Jay-Z", "Rap")
print(ninety_nine_problems.artists)
print(ninety_nine_problems.artist_count)

another_problem = Song("100 Problems", "Jay-Z", "Rap")
print(another_problem.genres)
print(another_problem.artist_count)

country_song = Song("Old Town Road", "Lil Nas X", "Country")
print(country_song.artists)
print(country_song.artist_count)

country_song = Song("Old Town Road", "Lil Nas X", "Rock")
print(country_song.artists)
print(country_song.artist_count)