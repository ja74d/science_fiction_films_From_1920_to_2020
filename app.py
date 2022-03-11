import requests
from bs4 import BeautifulSoup

source = requests.get("https://en.wikipedia.org/wiki/List_of_science_fiction_films_of_the_2010s").text
soup = BeautifulSoup(source, 'lxml')

table = soup.find('table', class_='wikitable')

# all movies
for films in table.find_all('i'):
    movie_name = films.text
#    print(movie_name)


# movie director
for directors in table.find_all('tr'):
    try:
        director = directors.find_all('td')[1].text
#        print(director)
    except:
        pass

# cast
for cast in table.find_all('tr'):
    try:
        cast_name = cast.find_all('td')[2].text
#        print(cast_name)
    except:
        pass

# country
for country in table.find_all('tr'):
    try:
        country_name = country.find_all('td')[3].text
#        print(country_name)
    except:
        pass

# subgenre/notes
for subgenre in table.find_all('tr'):
    try:
        subgenre_name = subgenre.find_all('td')[4].text
#        print(subgenre_name)
    except:
        pass
