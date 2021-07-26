import json
import requests
from bs4 import BeautifulSoup
from Task1 import movie_details
from Task4 import scrape_movie_details
from pprint import pprint

movie = movie_details
def get_movie_list_details():
    movie_list = []
    for i in movie[:10]:
        a = scrape_movie_details(i["Url"])
        movie_list.append(a)
    with open("saral_task5.json","w+") as file:
        json.dump(movie_list,file,indent=4)
    return movie_list
ten_movie_details = get_movie_list_details()

# here we call the function and if you want to see your output then print otherwise no need to print

