import requests
import csv
from bs4 import BeautifulSoup

csv_file = open('all.csv', 'w')

#source = requests.get("https://en.wikipedia.org/wiki/List_of_science_fiction_films_of_the_2010s").text
#soup = BeautifulSoup(source, 'lxml')

#table = soup.find('table', class_='wikitable')

# all movies
def info():
    for x in range(1920, 2020, 10):
        source = requests.get(f"https://en.wikipedia.org/wiki/List_of_science_fiction_films_of_the_{year}s").text
        soup = BeautifulSoup(source, 'lxml')

        table = soup.find('table', class_='wikitable')
        writer = csv.writer(csv_file)
        informations = writer.writerow(('movie_name', 'director', 'cast_name', 'country_name', 'subgenre_name'))
        for films in table.find_all('tr'):
            try:
                movie_name = films.find_all('td')[0].text
                #print(movie_name)

                # movie director
                director = films.find_all('td')[1].text
                #print(director)

                # cast
                cast_name = films.find_all('td')[2].text
                #print(cast_name)

                # country
                country_name = films.find_all('td')[3].text
                #print(country_name)

                # subgenre/notes
                subgenre_name = films.find_all('td')[4].text
                writer.writerow((movie_name, director, cast_name, country_name, subgenre_name))
                #print(subgenre_name)

                #print('\n')
                #print('----------------------------')
            except:
                pass
info()
