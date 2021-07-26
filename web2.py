from web1 import movie_data
import json
file1 = open("web1.json","r")
movies = json.load(file1)

def group_by_year(movies):
    emp_dic = {}
    for index in movies:
        movie_list = []
        year = index["Year"]
        if year not in  emp_dic:
            for k in movies:
                if year == k["Year"]:
                    movie_list.append(k)
            emp_dic[year] = movie_list
    with open("web2.json","w+")as file:
        json.dump(emp_dic,file,indent = 4)
        a = json.dumps(emp_dic)
year__ = group_by_year(movies = movie_data)


