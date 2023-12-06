

f = open(r"C:\Users\erijoh\OneDrive - ELU\Documents\Python\AoC-2023\6\test6_2.txt", "r")

total = 1

endtime = 30
timetobeat = 200

def beatenRaces(endtime,disttobeat):

    nwins = 0

    for x in range(endtime):

        dist = x*endtime - x**2

        if dist > disttobeat:
            nwins = nwins + 1

    return nwins


endtimes = []
timestobeat = []


ii = 0
for string in f:
    string = string.replace("\n","")
    string = string.split(" ")
    while("" in string):
        string.remove("")
    if ii == 0:
        endtimes = string[1:]
    if ii == 1:
        timestobeat = string[1:]
    ii = ii+1




for i in range(len(string)-1):
    endtime = int(endtimes[i])
    timetobeat = int(timestobeat[i])
    n = beatenRaces(endtime,timetobeat)
    total = total*n



print(total)