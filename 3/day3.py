import numpy as np

def checkNb(i,j):
    status = False
    nb1 = matrix[max(i-1, 0), max(j-1, 0)]
    nb2 = matrix[max(i-1, 0), j]
    nb3 = matrix[max(i-1, 0), min(j+1, cols-1)]
    nb4 = matrix[i, max(j-1, 0)]
    nb5 = matrix[i, min(j+1, cols-1)]
    nb6 = matrix[min(i+1, rows-1), max(j-1, 0)]
    nb7 = matrix[min(i+1, rows-1), j]
    nb8 = matrix[min(i+1, rows-1), min(j+1, cols-1)]
    for nb in [nb1, nb2, nb3, nb4, nb5, nb6, nb7, nb8]:
            if any(c in special_characters for c in nb):
                status = True
    return status
             

path = r"C:\Users\Erik\Documents\Python\AoC-2023\3\input3.txt"

with open(path, 'r') as file:
    lines = [list(line.strip()) for line in file]

matrix = np.array(lines)

rows, cols = matrix.shape

special_characters = "!@#$%^&*()-+?_=,<>/"
special_characters = [char for char in special_characters]

allvec = []
i = 0
j = 0
test = 0
while i < rows:
    while j < cols:
        element = matrix[i, j]
        test=test+1
        if element.isdigit():
            startdigit = j
            hh = int(j)
            numlength = 0
            localstatus = False
            while matrix[i,hh].isdigit():
                if checkNb(i,hh):
                     localstatus = True
                numlength = numlength + 1
                hh = hh+1
                if hh == cols:
                    break
            j = j+numlength
            if localstatus:
                numnum = []
                for u in range(numlength):
                    numnum.append(matrix[i,startdigit+u])
                allvec.append(int(''.join(numnum)))
        j = j+1
    j = 0
    i = i+1

print(allvec)
print(sum(allvec))

