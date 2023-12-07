# import numpy as np

# def shift_right(lst, n):
#     n = n % len(lst)  # Ensure n is within the range of the list length
#     shifted_list = lst[-n:] + lst[:-n]
#     return shifted_list

# def shift_left(lst, n):
#     n = n % len(lst)  # Ensure n is within the range of the list length
#     shifted_list = lst[n:]# + lst[:n]
#     return shifted_list

# f = open(r"C:\Users\erijoh\OneDrive - ELU\Documents\Python\AoC-2023\5\test5.txt", "r")


# seed_to_soil_map = []

# strings = f.readlines()

# for i in range(len(strings)):
#     string = strings[i]
#     if string.startswith("seed-to-soil"):
#         jj = i+1
#         while strings[jj] != "\n":
#             seed_to_soil_map.append(strings[jj].replace("\n",""))
#             jj = jj+1


# print(seed_to_soil_map)
# seedvec = np.zeros([100,2])

# linvec = [*range(0,99)]

# linvec = shift_left(linvec,2)

