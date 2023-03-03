import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response =  requests.get(URL)
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")

movies = []

movies_names_data = soup.find_all(name="h3", class_="title")

for movie in movies_names_data:
    name = movie.getText()
    movies.append(name)
    # ordered_list = movies.reverse()

print(mo)


