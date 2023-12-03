import numpy as np


#Tanken är att göra liknande förra gången. Denna gången kollar man alla siffror och om de är granne med *. Om det är så så skickar checkNb med koordinaterna för grannarna (ett nummer kan ha flera grannar)
#Man får även se till att en granne endast förekommer en gång för alla siffror i numret. 
#Sedan sparas en numret i en vektor likt förut, men nu finns även en vektor som innehåller koordinater för grannstjärnor. Dessa vektorer är lika stora. De fleska nummer har inga grannar
#Sedan sorteras båda listorna enligt koordinatmönstret, så att alla koordinater kommer i ordning. Detta gör att koordinater som förekommer EXAKT två gånger hamnar bredvid varandra.
#Sist loopar man igenom koordinatvektorn och kollar så att koordinatlistan inte är tom, och att den förekommer exakt två gånger. Man sparar numrena som motsvarar detta villkor i en egen ny vektor.
#Sedan multiplicerar man varje nummer i den nya vektorm med sin granne och sen har man svaret. 

def checkNb(i,j):
    status = False
    starnb = []
    if matrix[max(i-1, 0), max(j-1, 0)] == "*":
        status = True
        starnb.append([max(i-1, 0), max(j-1, 0)])
    if matrix[max(i-1, 0), j] == "*":
        status = True
        starnb.append([max(i-1, 0), j])
    if matrix[max(i-1, 0), min(j+1, cols-1)] == "*":
        status = True
        starnb.append([max(i-1, 0), min(j+1, cols-1)])
    if matrix[i, max(j-1, 0)] == "*":
        status = True
        starnb.append([i, max(j-1, 0)])
    if matrix[i, min(j+1, cols-1)] == "*":
        status = True
        starnb.append([i, min(j+1, cols-1)])
    if matrix[min(i+1, rows-1), max(j-1, 0)] == "*":
        status = True
        starnb.append([min(i+1, rows-1), max(j-1, 0)])
    if matrix[min(i+1, rows-1), j] == "*":
        status = True
        starnb.append([min(i+1, rows-1), j])
    if matrix[min(i+1, rows-1), min(j+1, cols-1)] == "*":
        status = True
        starnb.append([min(i+1, rows-1), min(j+1, cols-1)])
    return starnb

path = r"C:\Users\Erik\Documents\Python\AoC-2023\3\input3.txt"

with open(path, 'r') as file:
    lines = [list(line.strip()) for line in file]

matrix = np.array(lines)

rows, cols = matrix.shape


testvec = []
starvec = []
numvec = []
i = 0
j = 0
test = 0
while i < rows:
    while j < cols:
        element = matrix[i, j]
        if element.isdigit():
            startdigit = j
            hh = int(j)
            numlength = 0
            tempvec = []
            while matrix[i,hh].isdigit():
                if checkNb(i,hh) != []:
                    testvec.append(checkNb(i,hh))
                    if checkNb(i,hh) not in tempvec:
                        tempvec.append(checkNb(i,hh))
                numlength = numlength + 1
                hh = hh+1
                if hh == cols:
                    break
            j = j+numlength
            starvec.append(tempvec)
            numnum = []
            for u in range(numlength):
                numnum.append(matrix[i,startdigit+u])
            numvec.append(int(''.join(numnum)))
        j = j+1
    j = 0
    i = i+1

numvec = [x for _,x in sorted(zip(starvec,numvec))]
starvec = sorted(starvec)

gearvec = []

for i in range(len(numvec)):
    if starvec[i] != []:
        if starvec.count(starvec[i]) == 2:
            gearvec.append(numvec[i])

total = 0
for q in range(len(gearvec)):
    if q%2 == 0:
        total = total + gearvec[q]*gearvec[q+1]
print(total)

