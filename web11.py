import json
with open("web5.json","r")as file:
    data = json.load(file)

def anlyse_movie_genre():
    i = 0
    dict1 = {}
    list = []
    count = 0
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    count5 = 0
    count6 = 0
    count7 = 0
    count8 = 0
    count9 = 0
    count10 = 0
    count11 = 0
    count12 = 0
    count13 =0
    count14 = 0
    while i < len(data):
        for key in data[i]:
            if key == "Genre":
                list.append(data[i][key])
                index = 0
                while index < len(list):
                    j = 0 
                    while j < len(list[index]):
                        if list[index][j] == "adventure":
                            count += 1
                            dict1[list[index][j]] = count
                        elif list[index][j] == " animation":
                            count1 += 1
                            dict1[list[index][j]] = count1
                        elif list[index][j] == " fantasy":
                            count2 += 1
                            dict1[list[index][j]] = count2
                        elif list[index][j] == " comedy":
                            count3 += 1
                            dict1[list[index][j]] = count3
                        elif list[index][j] == " action":
                            count4 += 1
                            dict1[list[index][j]] = count4
                        elif list[index][j] == " kids & family":
                            count5 += 1
                            dict1[list[index][j]] = count5
                        elif list[index][j] == " music":
                            count6 += 1
                            dict1[list[index][j]] = count6
                        elif list[index][j] == " musical":
                            count7 += 1
                            dict1[list[index][j]] = count7
                        elif list[index][j] == " sci-fi":
                            count8 += 1
                            dict1[list[index][j]] = count8
                        elif list[index][j] == "drama":
                            count9 += 1
                            dict1[list[index][j]] = count9
                        elif list[index][j] == "anime":
                            count10 += 1
                            dict1[list[index][j]] = count10
                        elif list[index][j] == " war":
                            count11 += 1
                            dict1[list[index][j]] = count11
                        elif list[index][j] ==  " documentary":
                            count12 += 1
                            dict1[list[index][j]] = count12
                        elif list[index][j] == " biography":
                            count13 += 1
                            dict1[list[index][j]] = count13
                        elif list[index][j] == "other":
                            count14 += 1
                            dict1[list[index][j]] = count14
                        j += 1
                    index += 1
        i += 1             
    print(dict1)  
    with open("web11.json","w")as f:
        json.dump(dict1,f,indent = 4)
anlyse_movie_genre()
