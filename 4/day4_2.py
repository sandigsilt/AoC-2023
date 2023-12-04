import numpy as np

f = open(r"C:\Users\erijoh\OneDrive - ELU\Documents\Python\AoC-2023\4\input4.txt", "r")

def countwin(card):
    string = card.split(":")[1]
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
    return tempcount


cardvec = []

for string in f:
    cardvec.append(string)

num_of_card_vec = np.zeros(len(cardvec))

cardindex = 0
for string in cardvec:

    tempcount = countwin(string)
    if cardindex > 0:
        for ii in range(int(num_of_card_vec[cardindex])+1):
            for j in range(tempcount):
                num_of_card_vec[cardindex+j+1] = num_of_card_vec[cardindex+j+1] + 1
    else:
        for j in range(tempcount):
                num_of_card_vec[j+1] = num_of_card_vec[j+1] + 1

    cardindex = cardindex + 1


print((num_of_card_vec+1).astype(int))
print(int(sum(num_of_card_vec+1)))
