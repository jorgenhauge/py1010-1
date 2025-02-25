import numpy as np

arr = np.zeros((4, 3))
for i in range(1, 4+1):
    for j in range(1, 3+1):
        arr[i-1][j-1] = i + j

print(arr)
