from Task1 import movie_details
import json

def group_by_year(movies):
    emp_dic = {}
    empty=[]
    for i in movies:
        year = []
        for j in movies:
            if i["Year"] == j["Year"]:
                year.append(i)
                emp_dic[i["Year"]] = year
                break
    with open("saral_task2.json","w+")as file:
        json.dump(emp_dic,file,indent=4)
        return emp_dic

Year_ = group_by_year(movies = movie_details)

# here we call the function and if you want to see your output then print otherwise no need to print

