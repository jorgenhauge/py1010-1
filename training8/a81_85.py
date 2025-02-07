import numpy as np

for i in range(105, 37-2, -2):
    print(i)

s = 0
for i in range(14, 109):
    if i == 24:
        print("Twentyfour")
    else:
        s += i
print(s)

start = 0
arr = np.zeros(31)

for idx, elem in enumerate(arr):
    arr[idx] = 1 / start
    start += 1
