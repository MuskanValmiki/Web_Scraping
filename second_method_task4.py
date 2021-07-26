from Task1 import movie_details
import requests
from bs4 import BeautifulSoup
import json
from pprint import pprint

data = requests.get("https://www.imdb.com/india/top-rated-indian-movies/")
movie_data = BeautifulSoup(data.text,"html.parser")

user_input = input("enter any movies name=")

def scrape_movie_details():
    dict = {}
    for i in range(0,len(movie_details)):
        for j in movie_details[i]:
            if movie_details[i]["Name"] == user_input:
                data1 = requests.get(movie_details[i]["Url"])
                url_details = BeautifulSoup(data1.text,"html.parser")

    rank = url_details.find("span",class_= "AggregateRatingButton__RatingScore-sc-1il8omz-1 fhMjqK").get_text()
    dict["Rank"] = rank

    name = url_details.find("h1",class_= "TitleHeader__TitleText-sc-1wu6n3d-0 dxSWFG").get_text()
    dict["Name"] = name

    director = url_details.find("a",class_= "ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link").get_text()
    dict["Director"] = director

    run_time = url_details.find("div",class_="TitleBlock__TitleMetaDataContainer-sc-1nlhx7j-4 cgfrOx").get_text()[10:]
    run_hour = int(run_time[0])*60
    movie_run_time = 0
    if "min" in run_time:
        run_time_min = int(run_time[3:].strip("min"))
        movie_run_time = run_hour + run_time_min
    else:
        movie_run_time = run_hour
    dict["Time"] = movie_run_time,"minutes"

    bio = url_details.find("div",class_="ipc-html-content ipc-html-content--base").get_text()
    dict["Bio"] = bio

    poster_img_url = url_details.find("div",class_="Media__PosterContainer-sc-1x98dcb-1 dGdktI").a["href"]
    dict["Poster_img_url"] = poster_img_url


    genre = url_details.find("div",class_="ipc-chip-list ipc-chip-list--wrap GenresAndPlot__GenresChipList-cum89p-6 fLrtBh").get_text()
    dict["Genre"] = genre

    maindiv = url_details.select("div[data-testid='title-details-section']")
    for key in maindiv:
        find_all_li = key.select("li[data-testid='title-details-languages']")
        for li_lan in find_all_li:
            lan = li_lan.find_all("li",class_="ipc-inline-list__item")
            lanuage = [d.get_text() for d in lan]
            dict["Language"] = lanuage
    
    subdiv = url_details.select("li[data-testid='title-details-origin']")
    for c in subdiv:
        find1_all_li = c.find_all("li",class_="ipc-inline-list__item")
        country = [d.get_text() for d in find1_all_li]
        dict["Country"] = country

    with open("second_method_saral_task4.json","w+") as file:
        json.dump(dict,file,indent=4)
    return dict

scrape_movie_details()

# here we call the function if you want to see output then print otherwise not need to print
