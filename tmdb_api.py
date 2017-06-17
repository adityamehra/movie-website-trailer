import requests

def get_data_from_api(movie_id):

        # This is api end-point
        url = "https://api.themoviedb.org/3/movie/" + movie_id + "?api_key=ab63b9424c2cb4a17eb0533179659cb5"

        # Gets the response from the url
        response = requests.request("GET", url)

        # Changes the json response to python dictionary
        data = response.json()

        # return the python dictionary
        return data
