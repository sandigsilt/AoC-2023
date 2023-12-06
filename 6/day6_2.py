

f = open(r"C:\Users\erijoh\OneDrive - ELU\Documents\Python\AoC-2023\6\input6.txt", "r")

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

megaendtime = ""
megatimetobeat = ""

for i in endtimes:
    megaendtime = megaendtime + i
for j in timestobeat:
    megatimetobeat = megatimetobeat + j


print(megaendtime)
print(megatimetobeat)

n = beatenRaces(int(megaendtime),int(megatimetobeat))

print(n)