f = open(r"C:\Users\Erik\Documents\Python\AoC-2023\7\input7.txt", "r")

from itertools import product
import math

values = ["J","2","3","4","5","6","7","8","9","T","Q","K","A"]
hands = []
bids = []

hand = "5JJJJ"

def jokerShuffle(hand):
    listlist = []
    for value in values:
        listlist.append(hand.count(value))

    numJ = listlist[0]

    handvec = [char for char in hand]

    indexes = [i for i, v in enumerate(handvec) if v == "J"]


    testtest = []
    for i in range(numJ):
        testtest.append(values[1:])

    test = list(product(*testtest))


    localscore_prev = 0
    localscore = 0

    for i in range(len(test)):
        jjj = 0
        dfg = test[i]
        for index in indexes:
            handvec[index] = dfg[jjj]
            jjj = jjj+1
        listlist = []
        for value in values:
            listlist.append(handvec.count(value))

        if listlist.count(5) == 1:

            localscore = 7

        if listlist.count(4) == 1 and listlist.count(5) == 0:

            localscore = 6

        if listlist.count(2) == 1 and listlist.count(3) == 1:

            localscore = 5

        if listlist.count(3) == 1 and listlist.count(2) == 0:

            localscore = 4

        if listlist.count(2) == 2:

            localscore = 3

        if listlist.count(2) == 1 and listlist.count(3) == 0:

            localscore = 2

        if listlist.count(1) == 5:

            localscore = 1

        if localscore > localscore_prev:
            localscore_prev = localscore

    #print(localscore_prev)
    return localscore_prev












jokerShuffle(hand)

for string in f:
    temphand = string.split(" ")[0]
    tempbid = string.split(" ")[1]
    hands.append(temphand)
    bids.append(int(tempbid))

handscore = []



for hand in hands:
    listlist = []
    for value in values:
        listlist.append(hand.count(value))

    handvec = [char for char in hand]

    if handvec[0] == 0:

        if listlist.count(5) == 1:

            localscore = 7e6 + values.index(handvec[0])*1e4 + values.index(handvec[1])*1e2 + values.index(handvec[2])*1e0 + values.index(handvec[3])*1e-2 + values.index(handvec[4])*1e-4
            handscore.append(localscore)

        if listlist.count(4) == 1 and listlist.count(5) == 0:

            localscore = 6e6 + values.index(handvec[0])*1e4 + values.index(handvec[1])*1e2 + values.index(handvec[2])*1e0 + values.index(handvec[3])*1e-2 + values.index(handvec[4])*1e-4
            handscore.append(localscore)


        if listlist.count(2) == 1 and listlist.count(3) == 1:

            localscore = 5e6 + values.index(handvec[0])*1e4 + values.index(handvec[1])*1e2 + values.index(handvec[2])*1e0 + values.index(handvec[3])*1e-2 + values.index(handvec[4])*1e-4
            handscore.append(localscore)


        if listlist.count(3) == 1 and listlist.count(2) == 0:

            localscore = 4e6 + values.index(handvec[0])*1e4 + values.index(handvec[1])*1e2 + values.index(handvec[2])*1e0 + values.index(handvec[3])*1e-2 + values.index(handvec[4])*1e-4
            handscore.append(localscore)

        if listlist.count(2) == 2:

            localscore = 3e6 + values.index(handvec[0])*1e4 + values.index(handvec[1])*1e2 + values.index(handvec[2])*1e0 + values.index(handvec[3])*1e-2 + values.index(handvec[4])*1e-4
            handscore.append(localscore)


        if listlist.count(2) == 1 and listlist.count(3) == 0:

            localscore = 2e6 + values.index(handvec[0])*1e4 + values.index(handvec[1])*1e2 + values.index(handvec[2])*1e0 + values.index(handvec[3])*1e-2 + values.index(handvec[4])*1e-4
            handscore.append(localscore)

        if listlist.count(1) == 5:

            localscore = 1e6 + values.index(handvec[0])*1e4 + values.index(handvec[1])*1e2 + values.index(handvec[2])*1e0 + values.index(handvec[3])*1e-2 + values.index(handvec[4])*1e-4
            handscore.append(localscore)

    else:

        jokerscore = jokerShuffle(hand)

        if jokerscore == 7:

            localscore = 7e6 + values.index(handvec[0])*1e4 + values.index(handvec[1])*1e2 + values.index(handvec[2])*1e0 + values.index(handvec[3])*1e-2 + values.index(handvec[4])*1e-4
            handscore.append(localscore)

        if jokerscore == 6:

            localscore = 6e6 + values.index(handvec[0])*1e4 + values.index(handvec[1])*1e2 + values.index(handvec[2])*1e0 + values.index(handvec[3])*1e-2 + values.index(handvec[4])*1e-4
            handscore.append(localscore)


        if jokerscore == 5:

            localscore = 5e6 + values.index(handvec[0])*1e4 + values.index(handvec[1])*1e2 + values.index(handvec[2])*1e0 + values.index(handvec[3])*1e-2 + values.index(handvec[4])*1e-4
            handscore.append(localscore)


        if jokerscore == 4:

            localscore = 4e6 + values.index(handvec[0])*1e4 + values.index(handvec[1])*1e2 + values.index(handvec[2])*1e0 + values.index(handvec[3])*1e-2 + values.index(handvec[4])*1e-4
            handscore.append(localscore)

        if jokerscore == 3:

            localscore = 3e6 + values.index(handvec[0])*1e4 + values.index(handvec[1])*1e2 + values.index(handvec[2])*1e0 + values.index(handvec[3])*1e-2 + values.index(handvec[4])*1e-4
            handscore.append(localscore)


        if jokerscore == 2:

            localscore = 2e6 + values.index(handvec[0])*1e4 + values.index(handvec[1])*1e2 + values.index(handvec[2])*1e0 + values.index(handvec[3])*1e-2 + values.index(handvec[4])*1e-4
            handscore.append(localscore)

        if jokerscore == 1:

            localscore = 1e6 + values.index(handvec[0])*1e4 + values.index(handvec[1])*1e2 + values.index(handvec[2])*1e0 + values.index(handvec[3])*1e-2 + values.index(handvec[4])*1e-4
            handscore.append(localscore)



hands = [x for _,x in sorted(zip(handscore,hands))]
bids = [x for _,x in sorted(zip(handscore,bids))]

handscore = sorted(handscore)


total = 0

for i in range(len(bids)):
    total = total + (i+1)*bids[i]

print(total)


