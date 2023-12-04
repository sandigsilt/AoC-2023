f = open(r"C:\Users\erijoh\OneDrive - ELU\Documents\Python\AoC-2023\4\input4.txt", "r")

total = 0

for string in f:

    string = string.split(":")[1]
    string = string[1:]

    winning = string.split("|")[0]
    winning = winning.split(" ")
    winning = [int(i) for i in winning if i]

    your = string.split("|")[1]
    your = your.split(" ")
    your = [int(i) for i in your if i]

    tempcount = 0

    for num in your:
        if num in winning:
            tempcount = tempcount + 1
    if tempcount == 0:
        total = total + 0
    else:
        total = total + 2**(tempcount-1)


print(total)
