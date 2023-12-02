f = open(r"C:\Users\Erik\Documents\Python\AoC-2023\2\input2.txt", "r")


total = 0


for string in f:
    gameid = int((string.split(":")[0]).split(" ")[1])
    #content.append(string.split(":")[1])

    pulls = string.split(":")[1].split(";")
    contents = []
    tempwin = True
    maxred = 0
    maxgreen = 0
    maxblue = 0
    for pull in pulls:
        contents = pull.split(",")
        
        for cubes in contents:
            cubes = cubes[1:]

            test = cubes.split(" ")
            #print(test)
            num = int(cubes.split(" ")[0])
            cubecolor = cubes.split(" ")[1]
            cubecolor = cubecolor.replace("\n", "")
            #print(cubecolor)

            #print(cubecolor + str(num))
            if cubecolor == "red":
                if num > maxred:
                    maxred = num

            if cubecolor == "green":
                if num > maxgreen:
                    maxgreen = num

            if cubecolor == "blue":
                if num > maxblue:
                    maxblue = num


    # print("red: " + str(maxred))
    # print("green: " + str(maxgreen))
    # print("blue: " + str(maxblue))

    power = maxred*maxgreen*maxblue
    total = total + power

print(total)
    

