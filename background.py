import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djiboutimovies.settings")
import django
django.setup()
import requests
import json
import os
import shutil
import sqlite3
import dbutils
import sys
from movies.models import Movie


INPUT_FILE_FOLDER = "/Users/augiedoebling/media/"
OUTPUT_FILE_FOLDER = "/Users/augiedoebling/media/moved/"


def run():
    for file in os.listdir(INPUT_FILE_FOLDER):
        if(isMovie(file)):
            #shutil.move(INPUT_FILE_FOLDER+file, OUTPUT_FILE_FOLDER+file)
            try:
                saveMovieInfo(file.split(".")[0], OUTPUT_FILE_FOLDER+file)
            except:
                print(file)


def genMovieInfo(title, year, fileurl):
    title = title.replace(' ', "%20")
    requrl = ""
    if(year != None):
        requrl = "http://www.omdbapi.com/?t=" + title + "&y=" + year + "&plot=short&r=json"
    else:
        requrl = "http://www.omdbapi.com/?t=" + title + "&plot=short&r=json"

    response = requests.get(requrl)
    movie = json.loads(response.text)

    if(movie["Response"] == "False"):
        print("cant get " + requrl)
        raise FileNotFoundError

    # print(movie)

    genres = movie["Genre"].split(",")
    one = genres[0] if len(genres) > 0 else ""
    two = genres[1] if len(genres) > 1 else ""
    three = genres[2] if len(genres) > 2 else ""
    runtime = movie["Runtime"][:len(movie["Runtime"])-4]
    sep = "', '"

    return (movie["Title"],
            movie["Year"],
            runtime,
            one.replace("-", "").strip(),
            two.replace("-", "").strip(),
            three.replace("-", "").strip(),
            movie["imdbRating"],
            movie["Rated"],
            movie["Plot"].replace("'", ""),
            movie["Poster"],
            fileurl)

    # return ("'" + movie["Title"] + sep +
    #         movie["Year"] + sep +
    #         runtime + sep +
    #         one.replace("-", "").strip() + sep +
    #         two.replace("-", "").strip() + sep +
    #         three.replace("-", "").strip() + sep +
    #         movie["imdbRating"] + sep +
    #         movie["Rated"] + sep +
    #         movie["Plot"].replace("'", "") + sep +
    #         movie["Poster"] + sep +
    #         fileurl + "'")


def saveMovieInfo(filename, fileurl):
    db = sqlite3.connect("db.sqlite3")
    count = int(db.execute("SELECT count(*) from movies_movie").fetchall()[0][0])

    title = ""
    year = filename[len(filename)-4:]
    try:
        int(year)
        title = filename[:len(filename) - 5]
    except:
        title = filename
        year = None

    if(dbutils.doesmovieexist(title, year)):
        return

    movtup = genMovieInfo(title, year, fileurl)
    #print(movtup)

    p = Movie(title=movtup[0], year=movtup[1], running_time_min=movtup[2], genre_one=movtup[3], genre_two=movtup[4],
              genre_three=movtup[5], imdb_rating=movtup[6], rating=movtup[7], description=movtup[8], img_url=movtup[9],
              file_url=movtup[10])
    p.save()

def isMovie(file):
    formats = ["avi", "flv", "m4v", "mkv", "mov", "mp4", "m4v", "mpg", "wmv"]
    for form in formats:
        if(file.endswith(form)):
            return True
    return False

if __name__ == "__main__":
    if(sys.argv[1] == "run"):
        run()