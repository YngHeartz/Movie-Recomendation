import requests

API_KEY = 'df7cb704b97a64416b2429bd03b5171e'

movie_search = input("What movie are you looking for?")

movie_information = requests.get(f"https://api.themoviedb.org/3/search/{movie_search}?")

print(f"You are looking for {movie_search}, The basic information about this movie is: {movie_information}")

url = (f"https://api.themoviedb.org/3/search/movie?query={movie_search}&api_key=df7cb704b97a64416b2429bd03b5171e")

response = requests.get(url)

print(response.text)