import requests
from bs4 import BeautifulSoup
from pprint import pprint
url  =  requests.get("https://www.w3schools.com/python/python_intro.asp")
data  = BeautifulSoup(url.text,"html.parser")
# pprint(data)

data1 = data.find("a",href="python_variables.asp",target="_top").get_text()
pprint(data1)

data2 = data.find("a",href="python_variables_names.asp",target="_top").get_text()
pprint(data2)

data3 = data.find("a",href="python_variables_multiple.asp",target="_top").get_text()
pprint(data3)

data4 = data.find("a",href="python_variables_output.asp",target="_top").get_text()
pprint(data4)

data5 = data.find("a",href="python_variables_global.asp",target="_top").get_text()
pprint(data5)

data6 = data.find("a",href="python_variables_exercises.asp",target="_top").get_text()
pprint(data6)

data7 = data.find("a",href="python_datatypes.asp",target="_top").get_text()
pprint(data7)
