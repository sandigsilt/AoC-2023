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

def replaceNum(string):
    string = string.replace(["one","two"], ["1","2"]) 

f = open(r"C:\Users\erijoh\OneDrive - ELU\Documents\Python\AoC-2023\1\input1_2.txt", "r")

#for string in f:
total = 0
newstr = ""
for string in f:
    for i in range(7):
        indexvec = []
        valuevec = []
        keylength = []
        for key, value in repdict.items(): 
            try:
                #print(string.index(key))
                indexvec.append(string.index(key))
                valuevec.append(value)
                keylength.append(len(key))
                #newstring = string[string.index(key):] + string[string.index(key):string.index(key)+len(key)] + string[:string.index(key)+len(key)]
            except:
                #print("hittas ej")
                pass
        valuevec = [x for _, x in sorted(zip(indexvec, valuevec))]
        keylength = [x for _, x in sorted(zip(indexvec, keylength))]
        indexvec = sorted(indexvec)

        #teststr = string[:indexvec[0]] + string[indexvec[0]:indexvec[0]+keylength[0]] + string[indexvec[0]+keylength[0]:]
        try:
            string = string[:indexvec[0]] + valuevec[0] + string[indexvec[0]+keylength[0]:]
        except:
            break

    #print(string)
    digitvec = []
    for char in string:
        if char.isdigit():
            digitvec.append(char)
    
    tempnum = int(digitvec[0] + digitvec[-1])

    total = total + tempnum


print(total)



#     digitvec = []
#     for char in string:
#         if char.isdigit():
#             digitvec.append(char)
    
#     num = int(digitvec[0] + digitvec[-1])
#     total = total + num

# print(total)


