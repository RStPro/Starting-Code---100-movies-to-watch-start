import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response =  requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

movies_data = soup.find_all(name="h3", class_="title")

movie_titles = [movie.getText() for movie in movies_data]

# movie_titles.reverse()
movies = movie_titles[::-1]

with open("movies.txt", mode="w") as file:
    file.writelines('\n'.join(movies))