import json
with open("web5.json","r")as f:
    data = json.load(f)

def analyse_movie_language(data):
    language_dic = {}
    for dic in data:
        if "language" in dic:
            language = dic["language"]
            if language not in language_dic:
                language = dic["language"]
                language_dic[language] = 1
            else:
                language_dic[language] += 1
        else:
            continue
    with open("web6.json","w+") as file6:
        json.dump(language_dic,file6,indent = 4)
analyse_movie_language(data)

