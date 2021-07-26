# Apple i phone code 
import requests
from bs4 import BeautifulSoup
from pprint import pprint
 
url = requests.get("https://www.flipkart.com/apple-iphone-11-red-64-gb/p/itmc3935326f2feb?pid=MOBFWQ6BYYV3FCU7&lid=LSTMOBFWQ6BYYV3FCU7JCCDZJ&marketplace=FLIPKART&q=iphone+11&store=tyy%2F4io&srno=s_1_2&otracker=AS_QueryStore_OrganicAutoSuggest_1_6_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_6_na_na_na&fm=SEARCH&iid=650b9660-6749-4250-85eb-b450a2efa3c8.MOBFWQ6BYYV3FCU7.SEARCH&ppt=sp&ppn=sp&ssid=2jch47tjog0000001622171948056&qH=f6cdfdaa9f3c23f3")
data = BeautifulSoup(url.text,"html.parser")
# print(data)
# print(type(data))

def scrape_data():
    a=[]
    Name = data.find("span",class_ = "B_NuCI").get_text()[:-12]
    a.append(Name)
    # print(Name)

    Colour = data.find("span",class_ = "B_NuCI").get_text()[17:-8]
    a.append(Colour)
    # print(Colour)

    Storege = data.find("span",class_ = "B_NuCI").get_text()[21:-1].strip()
    a.append(Storege)
    # print(Storege)

    Price = data.find("div",class_ = "_30jeq3 _16Jk6d").get_text()
    a.append(Price)
    # print(Price)

    Rating = data.find("div",class_ = "_3LWZlK").get_text()
    a.append(Rating)
    # print(Rating)

    Display = data.find("div",class_ = "_2418kt").get_text()[9:53]
    a.append(Display)
    # print(Display)

    Camera = data.find("div",class_ = "_2418kt").get_text()[54:-22].strip()
    a.append(Camera)
    # print(Camera)

    Processor = data.find("div",class_ = "_2418kt").get_text()[-22:].strip()
    a.append(Processor)
    # print(Processor)
    
    index = 0
    dict = {}
    list = ["name","colour","storage","price","rating","display","camera","processor"]
    while index < len(list):
        dict[list[index]] = a[index]
        index += 1
    pprint(dict)    

scrape_data()

# nname camera rating price display battery