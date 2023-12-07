f = open(r"C:\Users\erijoh\OneDrive - ELU\Documents\Python\AoC-2023\7\input7.txt", "r")


values = ["2","3","4","5","6","7","8","9","T","J","Q","K","A"]
hands = []
bids = []


for string in f:
    temphand = string.split(" ")[0]
    tempbid = string.split(" ")[1]
    hands.append(temphand)
    bids.append(int(tempbid))

handscore = []


#DETTA ÄR RIKTIGA POKERREGLER. SKRIV OM

for hand in hands:
    listlist = []
    for value in values:
        listlist.append(hand.count(value))

    if listlist.count(5) == 1:


        localscore = 7e6 + listlist.index(5)*1e3
        handscore.append(localscore)

    if listlist.count(4) == 1 and listlist.count(5) == 0:

        
        localscore = 6e6 + listlist.index(4)*1e3 + listlist.index(1)*1
        handscore.append(localscore)


    if listlist.count(2) == 1 and listlist.count(3) == 1:
        localscore = 5e6 + listlist.index(3)*1e3 + listlist.index(2)
        handscore.append(localscore)


    if listlist.count(3) == 1 and listlist.count(2) == 0:

        indexes = [i for i, v in enumerate(listlist) if v == 1]
        indexes = sorted(indexes)

        localscore = 4e6 + listlist.index(3)*1e3 + indexes[1]*1e2 + indexes[0]*1e1
        handscore.append(localscore)

    if listlist.count(2) == 2:


        indexes = [i for i, v in enumerate(listlist) if v == 2]

        localscore = 3e6 + max(indexes)*1e3 + min(indexes)
        handscore.append(localscore)


    if listlist.count(2) == 1 and listlist.count(3) == 0:

        indexes = [i for i, v in enumerate(listlist) if v == 1]
        indexes = sorted(indexes)

        localscore = 2e6 + listlist.index(2)*1e3 + indexes[2]*1e2 + indexes[1]*1e1 + indexes[0]*1e0
        handscore.append(localscore)

    if listlist.count(1) == 5:

        indexes = [i for i, v in enumerate(listlist) if v == 1]
        indexes = sorted(indexes)
        print(indexes)
        localscore = 1e6 + indexes[4]*1e3 + indexes[3]*1e2 + indexes[2]*1e1 + indexes[1]*1e0 + indexes[0]*1e-1
        handscore.append(localscore)



hands = [x for _,x in sorted(zip(handscore,hands))]
bids = [x for _,x in sorted(zip(handscore,bids))]

handscore = sorted(handscore)

for i in range(len(hands)):
    print(hands[i] + " - " + str(handscore[i]))


total = 0

for i in range(len(bids)):
    total = total + (i+1)*bids[i]

print(total)