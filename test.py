import sys
import background

movies = [("Killers 2010", "test.mov"), ("Back to the Future 1985", "test.mov"),
          ("The Town 2010", "test.mov"), ("Predestination 2014", "test.mov")]

def main():
    command = sys.argv[1]
    if(command == "add"):
        if(int(sys.argv[2]) > 5):
            print("please < 5")
            return
        else:
            for i in range(int(sys.argv[2])):
                background.saveMovieInfo(movies[i][0], movies[i][1])

if __name__ == "__main__":
    main()
