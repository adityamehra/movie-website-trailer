import media
import fresh_tomatoes
import tmdb_api as tmdb

# dictionary to store the movie database (tmdb) ids for movies
# tmdb has ids for movies
tmdb_ids = {'beautiful_mind': '453-a-beautiful-mind',
            'jason_bourne': '324668-jason-bourne',
            'shawshank': '278-the-shawshank-redemption',
            'good_will': '489-good-will-hunting',
            'little_rascals': '10897-the-little-rascals',
            'karate_kid': '1885-the-karate-kid',
            'logan': '263115-logan',
            'pirates_2003': '22-pirates-of-the-caribbean-the-curse-of-the-black-pearl'
            }

# dictionary to store links to wikipedia posters of movies
link_to_posters = { 'beautiful_mind': 'https://upload.wikimedia.org/wikipedia/en/b/b8/A_Beautiful_Mind_Poster.jpg',
                    'jason_bourne': 'https://upload.wikimedia.org/wikipedia/en/b/b2/Jason_Bourne_%28film%29.jpg',
                    'shawshank': 'https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg',
                    'good_will': 'https://upload.wikimedia.org/wikipedia/en/b/b8/Good_Will_Hunting_theatrical_poster.jpg',
                    'little_rascals': 'https://upload.wikimedia.org/wikipedia/en/6/6f/Little_rascals_ver2.jpg',
                    'karate_kid': 'https://upload.wikimedia.org/wikipedia/en/a/a9/Karate_kid.jpg',
                    'logan': 'https://upload.wikimedia.org/wikipedia/en/3/37/Logan_2017_poster.jpg',
                    'pirates_2003': 'https://upload.wikimedia.org/wikipedia/en/8/89/Pirates_of_the_Caribbean_-_The_Curse_of_the_Black_Pearl.png'
                    }

# dictionary to store links to youtube trailers
link_to_trailers = {'beautiful_mind': 'https://www.youtube.com/watch?v=JV2PSWSyi0s',
                    'jason_bourne': 'https://www.youtube.com/watch?v=F4gJsKZvqE4',
                    'shawshank': 'https://www.youtube.com/watch?v=K_tLp7T6U1c',
                    'good_will': 'https://www.youtube.com/watch?v=PaZVjZEFkRs',
                    'little_rascals': 'https://www.youtube.com/watch?v=Svdb1XXVX_c',
                    'karate_kid': 'https://www.youtube.com/watch?v=n7JhKCQnEqQ',
                    'logan': 'https://www.youtube.com/watch?v=f7kIl-Q1yrA',
                    'pirates_2003': 'https://www.youtube.com/watch?v=2DXNYUTmGxA'
                    }

# list_of_movies to stores movies i.e. instance of Movie class
list_of_movies = []

# iterating over tmdb_ids
for id in tmdb_ids:

        # A Beautiful Mind
        # Getting the data from tmdb api for A Beautiful mind
        data_from_api = tmdb.get_data_from_api( tmdb_ids[id] )

        # Creating beautiful_mind
        # Instance of Movie

        # Each instance has title, stotyline, popularitym, year of release,
        # link to a poster and link to a youtube trailer

        # Extract year from 'release_date' by doing 'data_from_api['release_date'][:4]'
        # 'release_date' has format 'yyyy-mm-dd'
        movie = media.Movie(   data_from_api['title'],
                                        data_from_api['overview'],
                                        data_from_api['popularity'],
                                        data_from_api['release_date'][:4],
                                        link_to_posters[id],
                                        link_to_trailers[id])

        # Adding movie to the list
        list_of_movies.append(movie)

# Calling the open_movies_page function in fresh_tomatoes
# Passing the list_of_movies
fresh_tomatoes.open_movies_page( list_of_movies )
