import sqlite3
import sys


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

def main():
    command = sys.argv[1]
    if(command == "dbdrop"):
        dbdrop()
    elif(command == "select"):
        select()

if __name__ == "__main__":
    main()