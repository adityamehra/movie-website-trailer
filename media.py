import webbrowser as wb

# Creating a movie class
class Movie():

    # Constructor of the class
    # Takes title, stotyline, popularitym, year of release,
    # link to a poster and link to a youtube trailer

    def __init__(   self, movie_title, movie_storyline, movie_popularity,
                    movie_year, movie_poster, movie_trailer ):

        self.title = movie_title
        self.storyline = movie_storyline
        self.popularity = movie_popularity
        self.year = movie_year
        self.poster_image_url = movie_poster
        self.trailer_youtube_url = movie_trailer

    # instance method/member function to open a browser with trailer of the movie
    def showTrailer(self):
        wb.open(self.trailer_youtube_url)
