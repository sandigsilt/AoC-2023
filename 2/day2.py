f = open(r"C:\Users\Erik\Documents\Python\AoC-2023\2\input2.txt", "r")


total = 0


for string in f:
    gameid = int((string.split(":")[0]).split(" ")[1])
    #content.append(string.split(":")[1])

    pulls = string.split(":")[1].split(";")
    contents = []
    tempwin = True
    for pull in pulls:
        contents = pull.split(",")
        
        for cubes in contents:
            cubes = cubes[1:]

            num = int(cubes.split(" ")[0])
            cubecolor = cubes.split(" ")[1]
            if (num > 12 and cubecolor == "red") or (num > 13 and cubecolor == "green") or (num > 14 and cubecolor == "blue"):
                tempwin = False


    if tempwin:
        total = total + gameid
    


print(total)