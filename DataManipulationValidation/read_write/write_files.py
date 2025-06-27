1# open inputFile.txt with intention of reading it
inputFile = open("inputFile.txt", "r")

# open passFile.txt with intention of writing it
passFile = open("passFile.txt", "w")
# open failFile.txt with intention of writing it
failFile = open("failFile.txt", "w")

# loop through each line of inputFile
for line in inputFile:
    line_split = line.split()
    if line_split[2] == "P":
        passFile.write(line)
    else:
        failFile.write(line)        

inputFile.close()

# close pass and fail files
passFile.close()
failFile.close()