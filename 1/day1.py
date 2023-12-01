#Aoc day 1

repdict = {"one": "1",
           "two": "2",
           "three": "3",
           "four": "4",
           "five": "5",
           "six": "6",
           "seven": "7",
           "eight": "8",
           "nine": "9"}


f = open(r"C:\Users\erijoh\OneDrive - ELU\Documents\Python\AoC-2023\1\input1_2.txt", "r")

#for string in f:
total = 0
for string in f:
    for i in range(10):
        indexvec = []
        valuevec = []
        keylength = []
        for key, value in repdict.items(): 
            try:
                indexvec.append(string.index(key))
                valuevec.append(value)
                keylength.append(len(key))
            except:
                pass
        valuevec = [x for _, x in sorted(zip(indexvec, valuevec))]
        keylength = [x for _, x in sorted(zip(indexvec, keylength))]
        indexvec = sorted(indexvec)

        try:
            string = string[:indexvec[0]] + valuevec[0] + string[indexvec[0]+keylength[0]:]
        except:
            break

    digitvec = []
    for char in string:
        if char.isdigit():
            digitvec.append(char)
    
    tempnum = int(digitvec[0] + digitvec[-1])

    total = total + tempnum

print(total)

