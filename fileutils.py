import os
import sys
import smartmovie

minfilesize = 400000000

def moveAndRename(fromPathFile, toPath):
    filename = os.path.basename(fromPathFile)
    movie = smartmovie.parseFileName(filename)
    if movie is not None:
        newname = movie['Title'] + " " + movie['Year'] + fromPathFile[fromPathFile.rfind("."):]

        toPathFile = toPath + newname

        os.rename(fromPathFile, toPathFile)
        print "moved " + newname + " to " + toPath
        return (movie, toPathFile)


def mirgateDirectory(fromHomeDir, toPath):
    record = []

    # print os.listdir(fromHomeDir)
    homefiles = next(os.walk(fromHomeDir))[2]
    homedirs = next(os.walk(fromHomeDir))[1]

    for file in homefiles:
        if os.stat(fromHomeDir + file).st_size > minfilesize:
            # print(fromHomeDir + file)
            record.append(moveAndRename(fromHomeDir + file, toPath))

    for dir in homedirs:
        for file in next(os.walk(fromHomeDir + dir))[2]:
            if os.stat(fromHomeDir + dir + "/"+ file).st_size > minfilesize:
                # print(fromHomeDir + dir + "/" + file)
                record.append(moveAndRename(fromHomeDir + dir + "/" + file, toPath))
        for subdir in next(os.walk(fromHomeDir + dir))[1]:
            for subfile in next(os.walk(fromHomeDir + dir + "/" + subdir))[2]:
                if os.stat(fromHomeDir + dir + "/" + subdir + "/" + subfile).st_size > minfilesize:
                    # print(fromHomeDir + dir + "/" + subdir + "/" + subfile)
                    record.append(moveAndRename(fromHomeDir + dir + "/" + subdir + "/" + subfile, toPath))

    print "*****    Finished Migrating " + fromHomeDir + " to " + toPath + "    *****"

def main():
    command = sys.argv[1]
    if(command == "move"):
        moveAndRename(sys.argv[2], sys.argv[3])

    elif command == "migrate":
        mirgateDirectory(sys.argv[2], sys.argv[3])

if __name__ == "__main__":
    main()