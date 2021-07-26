import json
with open("web5.json","r")as f:
    data = json.load(f)

def analyse_movie_director(data):
    director_dict = {}
    i = 0
    while i < len(data):
        index = 0
        count = 0
        while index < len(data):
            if data[i]["director"] == data[index]["director"]:
                count += 1
                director = str(data[i]["director"])[0:]
                director_dict[director] = count
            index += 1    
        i += 1
    with open("web7.json","w+") as director_data:
        json.dump(director_dict,director_data,indent = 4)
    print(director_dict)     
analyse_movie_director(data)