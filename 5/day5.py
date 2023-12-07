size = 300

def shift_list(lst, start,dest, n):
    shifted_list = lst.copy()
    idx = start#lst.index(start)
    shifted_list[idx:idx+n] = [*range(dest,dest+n)]
    return shifted_list

def processMap(map,strings,k):
    k = k+1
    try:
        while strings[k] != "\n":
            map.append(strings[k].replace("\n",""))
            k = k+1
    except:
        pass

def sortMap(Map,List):
    new_list = List.copy()
    for localmap in Map:
        localmap = localmap.split(" ")
        localmap = list(map(int, localmap))
        new_list = shift_list(new_list,localmap[1],localmap[0],localmap[2])
    return new_list

f = open(r"C:\Users\Erik\Documents\Python\AoC-2023\5\test5.txt", "r")


seed_to_soil_map = []
soil_to_fertilizer_map = []
fertilizer_to_water_map = []
water_to_light_map = []
light_to_temperature_map = []
temperature_to_humudity_map = []
humidity_to_location_map = []

strings = f.readlines()

for i in range(len(strings)):
    string = strings[i]
    if string.startswith("seed-to-soil"):
        processMap(seed_to_soil_map,strings,i)

    if string.startswith("soil-to-fertilizer"):
        processMap(soil_to_fertilizer_map,strings,i)
    
    if string.startswith("fertilizer"):
        processMap(fertilizer_to_water_map, strings, i)

    if string.startswith("water"):
        processMap(water_to_light_map,strings,i)

    if string.startswith("light"):
        processMap(light_to_temperature_map,strings,i)

    if string.startswith("temperature"):
        processMap(temperature_to_humudity_map,strings,i)

    if string.startswith("humidity"):
        processMap(humidity_to_location_map,strings,i)


print(water_to_light_map)



seedlist = [*range(size)]
# soillist = [*range(size)]
# fertilizerlist = [*range(size)]
# waterlist = [*range(size)]



soillist = sortMap(seed_to_soil_map,seedlist)
fertilizerlist = sortMap(soil_to_fertilizer_map,soillist)
waterlist = sortMap(fertilizer_to_water_map,fertilizerlist)
lightlist = sortMap(water_to_light_map,waterlist)
temperaturelist = sortMap(light_to_temperature_map,lightlist)



print(seedlist[79])
print(soillist[79])
print(fertilizerlist[79])
print(lightlist[79])
print(temperaturelist[79])