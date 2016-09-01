import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djiboutimovies.settings")
import django
django.setup()
import sqlite3
import sys
from django.core import management
from djiboutimovies import settings
from movies.models import Movie


def setup():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djiboutimovies.settings")

def dbdrop():
    db = sqlite3.connect("db.sqlite3")
    db.execute("DELETE FROM movies_movie")
    db.commit()
    db.close()

def select():
    db = sqlite3.connect("db.sqlite3")
    results = db.execute("select * FROM movies_movie limit 5")
    for movie in results:
        print(movie)
    db.close()

def doesmovieexist(title, year):
    db = sqlite3.connect("db.sqlite3")
    results = None
    if(year == None):
        results = db.execute("select count(*) FROM movies_movie where title = '" + title + "'")
    else:
        results = db.execute("select count(*) FROM movies_movie where title = '" +
                             title + "' and year = '" + year + "'")
    for res in results:
        try:
            if(int(res[0]) == 1):
                db.close()
                return True
        except:
            continue
    db.close()
    return False

def query():
    res = Movie.objects.get(id='118')
    print(res.title)

def main():
    command = sys.argv[1]
    if(command == "dbdrop"):
        dbdrop()
    elif(command == "select"):
        select()
    elif(command == "exist"):
        print(doesmovieexist(sys.argv[2], sys.argv[3]))
    elif(command == "setup"):
        setup()
    elif (command == "query"):
        query()

if __name__ == "__main__":
    main()