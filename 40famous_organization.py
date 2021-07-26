import requests
from bs4 import BeautifulSoup

url  =  requests.get("https://scoop.eduncle.com/indian-national-government-organizations-agency")
data  =  BeautifulSoup(url.text,"html.parser")
# pprint(data)

maindiv  =  data.find("div", class_ =  "table-responsive")
trs  =  maindiv.find_all("tr")
# pprint(trs)

Serial_no  =  []
Organization_name  =  []
Abbreviation_name  =  []
Foundation_date  =  []
Logo_id  =  []
for i in trs:
    S_N  =  i.find("td",width = "115").get_text()
    Serial_no.append(S_N)

    Organization  =  i.find("td",width = "148").get_text()
    Organization_name.append(Organization)

    Abbreviation  =  i.find("td",width = "123").get_text()
    Abbreviation_name.append(Abbreviation)
    
    Foundation_Date   =  i.find("td",width = "122").get_text()
    Foundation_date.append(Foundation_Date)

    Logo  =  i.find("td",width = "116").get_text()
    Logo_id.append(Logo)

index  =  0
main_list  =  []
while index < len(Serial_no):
    dict  =  {}
    if index>0:
        dict["Serial_no"]  =  Serial_no[index]
        dict["Organization"]  =  Organization_name[index]
        dict["Abbreviation"]  =  Abbreviation_name[index]
        dict["Foundation_date"]  =  Foundation_date[index]
        dict["Logo"]  =  Logo_id[index]
        main_list.append(dict)
    index+=1
print(main_list)
