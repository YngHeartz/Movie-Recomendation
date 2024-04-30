import requests
# api connection
API_KEY = 'df7cb704b97a64416b2429bd03b5171e'
# Movie Input Title Information
movie_search = input("What movie are you looking for?")
# This will search the api and take the parameter given by the user from the movie_search input variable
movie_information = requests.get(f"https://api.themoviedb.org/3/search/{movie_search}?")
# Output the Movie Information in JSON format and print it out to the User
print(f"You are looking for {movie_search}, The basic information about this movie is: {movie_information}")
# retrieves the movie from the api and fills the title from the movie_search input variable
url = (f"https://api.themoviedb.org/3/search/movie?query={movie_search}&api_key=df7cb704b97a64416b2429bd03b5171e")

response = requests.get(url)

print(response.text)