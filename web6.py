import json
with open("web5.json","r")as f:
    data = json.load(f)

def analyse_movie_language(data):
    language_dict = {}
    count = 0
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    count5 = 0
    count6 = 0
    count7 = 0
    count8 = 0
    i = 0 
    while i < len(data):
        for key in data[i]:
            if data[i][key] == "English":
                count += 1
                language_dict[data[i][key]] = count
            elif data[i][key] == "English (United Kingdom)":
                count1 += 1
                language_dict[data[i][key]] = count1
            elif data[i][key] == "French (France)":
                count2 += 1  
                language_dict[data[i][key]] = count2
            elif data[i][key] == "Japanese":
                count3 += 1
                language_dict[data[i][key]] = count3
            elif data[i][key] == "Hebrew":
                count4 += 1
                language_dict[data[i][key]] = count4
            elif data[i][key] == "French (Canada)":
                count5 += 1
                language_dict[data[i][key]] = count5
            elif data[i][key] == "Bortuguese (Brazil)":
                count6 += 1
                language_dict[data[i][key]] = count6
            elif data[i][key] == "Unknown language":
                count7 += 1
                language_dict[data[i][key]] = count7
        i += 1
    print(language_dict)
    with open("web6.json","w+") as file6:
        json.dump(language_dict,file6,indent = 4)
analyse_movie_language(data)

