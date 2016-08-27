import requests
import json
import os
import shutil
import sqlite3

INPUT_FILE_FOLDER = "/Users/augiedoebling/media"
OUTPUT_FILE_FOLDER = "/Users/augiedoebling/media/moved"

GENRES = ["Short", "Drama", "Comedy", "Documentary", "Adult", "Action", "Romance", "Thriller", "Animation", "Family",
          "Crime", "Horror", "Music", "Adventure", "Fantasy", "Sci-Fi", "Mystery", "Biography", "Sport", "History",
          "Musical", "Western", "War", "Reality-TV", "News", "Talk-Show", "Game-Show"]

def run():
    for file in os.listdir(INPUT_FILE_FOLDER):
        if(isMovie(file)):
            shutil.move(INPUT_FILE_FOLDER+file, OUTPUT_FILE_FOLDER+file)
            saveMovieInfo(file, OUTPUT_FILE_FOLDER+file)


def genMovieInfo(filename, fileurl):
    title = filename[:len(filename)-5]
    title = title.replace(' ', "%20")
    year = filename[len(filename)-4:]
    requrl = "http://www.omdbapi.com/?t=" + title + "&y=" + year + "&plot=short&r=json"

    response = requests.get(requrl)
    movie = json.loads(response.text)

    if(movie["Response"] == "False"):
        raise FileNotFoundError

    # print(movie)

    genres = movie["Genre"].split(",")
    one = genres[0] if len(genres) > 0 else ""
    two = genres[1] if len(genres) > 1 else ""
    three = genres[2] if len(genres) > 2 else ""
    runtime = movie["Runtime"][:len(movie["Runtime"])-4]
    sep = "', '"

    return ("'" + movie["Title"] + sep +
            movie["Year"] + sep +
            runtime + sep +
            one + sep +
            two + sep +
            three + sep +
            movie["imdbRating"] + sep +
            movie["Rated"] + sep +
            movie["Plot"] + sep +
            movie["Poster"] + sep +
            fileurl + "'")


def saveMovieInfo(filename, fileurl):
    db = sqlite3.connect("db.sqlite3")
    count = int(db.execute("SELECT count(*) from movies_movie").fetchall()[0][0])
    insert = "INSERT INTO movies_movie VALUES ('" + str(count + 1) + "', " + genMovieInfo(filename, fileurl) + ")"
    message = db.execute(insert)
    db.commit()
    db.close()

def isMovie(file):
    formats = ["avi", "flv", "m4v", "mkv", "mov", "mp4", "m4v", "mpg", "wmv"]
    for form in formats:
        if(file.endswith(form)):
            return True
    return False

saveMovieInfo("the town 2010", "test.mov")