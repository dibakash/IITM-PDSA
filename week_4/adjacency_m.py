adjacency_list = {
    0: [1, 2, 4],
    1: [0, 2, 3, 4],
    2: [0, 1, 4, 6],
    3: [1, 4, 5, 6],
    4: [0, 1, 2, 3],
    5: [3],
    6: [2, 3],
}


import numpy as np

l = len(adjacency_list)

AM = np.zeros(shape=(l,l))
print(AM)

def a_m(AM, AL):
    for i in range(l):
        for j in range(l):
            if j in AL[i]:
                AM[i,j] = 1

a_m(AM,adjacency_list)

print(AM)
