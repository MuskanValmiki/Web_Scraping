import json
import requests
from bs4 import BeautifulSoup
from web1 import movie_data
from web4 import scrape_movie_details
movie = movie_data

def get_movie_list_details():
    movie_list = []
    for i in movie:
        link = i["Url"]
        list_of_movies = scrape_movie_details(i["Name"],link)
        movie_list.append(list_of_movies)
        return movie_list
    with open("web5.json","w+") as file5:
        json.dump(movie_list,file5,indent = 4)
all_movie_data = get_movie_list_details()
