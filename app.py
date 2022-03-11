import requests
from bs4 import BeautifulSoup

source = requests.get("https://en.wikipedia.org/wiki/List_of_science_fiction_films_of_the_2010s").text
soup = BeautifulSoup(source, 'lxml')

for films in soup.find_all('td'):
    movie_name = films.i.text
    print(movie_name)