import requests
from bs4 import BeautifulSoup
url = requests.get("https://www.flipkart.com/redmi-note-10-pro-glacial-blue-128-gb/p/itm04ba1f0aed358?pid=MOBGFDFYE7TFYZKV&lid=LSTMOBGFDFYE7TFYZKVFRRVV9&marketplace=FLIPKART&q=redmi+note+10+pro&store=tyy%2F4io&srno=s_1_1&otracker=AS_QueryStore_OrganicAutoSuggest_2_3_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_2_3_na_na_na&fm=SEARCH&iid=12360908-c2a3-41d5-b559-fb350dda2840.MOBGFDFYE7TFYZKV.SEARCH&ppt=hp&ppn=homepage&ssid=ng4okjejdc0000001623152160795&qH=20ef7d326dcad8f3")
data = BeautifulSoup(url.text,"html.parser")

dict = {}
mobile_name = data.find("span",class_="B_NuCI").get_text()[:6]
dict["Name"] = mobile_name

mobile_model = data.find("span",class_="B_NuCI").get_text()[6:18]
dict["Model"] = mobile_model

colour = data.find("h1",class_="yhB1nd").get_text()[19:31]
dict["Colour"] = colour

ram = data.find("div",class_="aMaAEs").get_text()[40:52].strip()
dict["Ram"] = ram

rating = data.find("div",class_="aMaAEs").get_text()[52:66]
dict["Rating"] = rating

price = data.find("div",class_="aMaAEs").get_text()[79:]
dict["Price"] = price

camera_GB = data.find("div",class_="_2418kt").get_text()[11:18]
dict["Camera"] = camera_GB

camera_rom = data.find("div",class_="_2418kt").get_text()[18:29]
dict["Camera_Rom"] = camera_rom

camera_hieght = data.find("div",class_="_2418kt").get_text()[30:41]
dict["Camera_height"] = camera_hieght

display = data.find("div",class_="_2418kt").get_text()[42:65]
dict["Display"] = display

battery = data.find("div",class_="_2418kt").get_text()[65:]
dict["Battery"] = battery
print(dict)


