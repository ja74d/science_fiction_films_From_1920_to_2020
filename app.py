import requests
from bs4 import BeautifulSoup

source = requests.get("https://en.wikipedia.org/wiki/List_of_science_fiction_films_of_the_2010s").text
soup = BeautifulSoup(source, 'lxml')

table = soup.find('table', class_='wikitable')

for films in table.find_all('i'):
    movie_name = films.text
#    print(movie_name)

for directors in table.find_all('tr'):
    director = directors.find_all('td')[1].text
    print(director)