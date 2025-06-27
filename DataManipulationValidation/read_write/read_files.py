inputFile = open("inputFile.txt", "r")
# print(inputFile.read())
for line in inputFile:
    line_split = line.split()
    if line_split[2] == "P":
        print(line)
inputFile.close()