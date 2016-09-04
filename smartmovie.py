import requests
import json

def parseFileName(filename):
    yearindex = -1

    name = filename[:filename.rfind(".")]
    # print name
    name = name.replace(".", " ")
    name = name.replace(",", " ")
    name = name.replace("-", " ")

    words = name.split()
    # print(words)

    # if yifi == words[len(words)-1]:
    for i in range(len(words)):
        # print words[i]
        if words[i].isdigit() and len(words[i]) == 4:
            yearindex = i
            break
        elif len(words[i]) == 6 and words[i][1:5].isdigit():
            words[i] = words[i][1:5]
            yearindex = i
            break

    # print(yearindex)

    if yearindex != -1:
        reqtitle = "%20".join(words[:yearindex])
        # readtitle = " ".join(words[:yearindex])
        movie = requestMovie(reqtitle, words[yearindex])

        if movie['Response'] == 'True':
            return movie

    print "******* Can not find movie" + filename
    return None





def requestMovie(title, year=None):
    requrl = ""
    if(year != None):
        requrl = "http://www.omdbapi.com/?t=" + title + "&y=" + year + "&plot=short&r=json"
    else:
        requrl = "http://www.omdbapi.com/?t=" + title + "&plot=short&r=json"

    response = requests.get(requrl)
    movie = json.loads(response.text)

    return movie
