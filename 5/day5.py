import numpy as np

f = open(r"C:\Users\erijoh\OneDrive - ELU\Documents\Python\AoC-2023\5\test5.txt", "r")


seed_to_soil_map = []

strings = f.readlines()

for i in range(len(strings)):
    string = strings[i]
    if string.startswith("seed-to-soil"):
        jj = i+1
        while strings[jj] != "\n":
            seed_to_soil_map.append(strings[jj].replace("\n",""))
            jj = jj+1


print(seed_to_soil_map)
seedvec = np.zeros([100,2])

for seedmap in seed_to_soil_map:
    seedmap = seedmap.split(" ")
    seedrange = seedmap[2]
    for i in range(int(seedrange)):
        seedvec[int(seedmap[0])+int(seedrange)] = 1 #int(seedvec[seedmap[0]+seedrange]) + seedrange
        pass

print(seedmap)