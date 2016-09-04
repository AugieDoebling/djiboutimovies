import os
import sys
import smartmovie

minfilesize = 400000000

def moveAndRename(fromPathFile, toPath):
    filename = os.path.basename(fromPathFile)
    movie = smartmovie.parseFileName(filename)
    if movie is not None:
        newname = movie['Title'] + " " + movie['Year'] + fromPathFile[fromPathFile.rfind("."):]

        toPathFile = toPath + "/" + newname

        if(fromPathFile != toPathFile):
            # os.rename(fromPathFile, toPathFile)
            print "moved " + newname + " to " + toPath
            return (movie, toPathFile)
        else:
            print("didnt move " + newname)
            return None



def mirgateDirectory(fromHomeDir, toPath):
    record = []

    # print os.listdir(fromHomeDir)
    homefiles = next(os.walk(fromHomeDir))[2]
    homedirs = next(os.walk(fromHomeDir))[1]

    for file in homefiles:
        pathFile = fromHomeDir + "/" + file
        if os.stat(pathFile).st_size > minfilesize and isMovie(pathFile):
            # print(pathFile)
            insert = moveAndRename(pathFile, toPath)
            if insert != None:
                record.append(insert)

    for dir in homedirs:
        for file in next(os.walk(fromHomeDir + "/" + dir))[2]:
            subPathFile = fromHomeDir + "/" + dir + "/" + file
            if os.stat(subPathFile).st_size > minfilesize and isMovie(subPathFile):
                # print(subPathFile)
                insert = moveAndRename(subPathFile, toPath)
                if insert != None:
                    record.append(insert)

        for subdir in next(os.walk(fromHomeDir + "/" + dir))[1]:
            for subfile in next(os.walk(fromHomeDir + "/" + dir + "/" + subdir))[2]:
                subSubPathFile = fromHomeDir + "/" + dir + "/" + subdir + "/" + subfile
                if os.stat(subSubPathFile).st_size > minfilesize and isMovie(subSubPathFile):
                    # print(subSubPathFile)
                    insert = moveAndRename(subSubPathFile, toPath)
                    if insert != None:
                        record.append(insert)

    print "*****    Finished Migrating " + fromHomeDir + " to " + toPath + "    *****"

def isMovie(file):
    formats = ["avi", "flv", "m4v", "mkv", "mov", "mp4", "m4v", "mpg", "wmv"]
    for form in formats:
        if(file.endswith(form)):
            return True
    return False

def main():
    command = sys.argv[1]
    if(command == "move"):
        moveAndRename(sys.argv[2], sys.argv[3])

    elif command == "migrate":
        mirgateDirectory(sys.argv[2], sys.argv[3])

    else:
        print("command does not exist : " + command)

if __name__ == "__main__":
    main()