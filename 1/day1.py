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

f = open(r"C:\Users\erijoh\OneDrive - ELU\Documents\Python\AoC-2023\1\test1_2.txt", "r")

#for string in f:

for string in f:

    for key, value in repdict.items(): 
        try:
            print(string.index(key))
        except:
            print("hittas ej")

    print(string)






#     digitvec = []
#     for char in string:
#         if char.isdigit():
#             digitvec.append(char)
    
#     num = int(digitvec[0] + digitvec[-1])
#     total = total + num

# print(total)


