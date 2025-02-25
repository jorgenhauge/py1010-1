import numpy as np

x = np.linspace(3, 22, 20)
s = 0
elems = []
index = 0

while s <= 150:
    elem = x[index]
    s += elem
    index += 1
    print(s)
    elems.append(elem)
print(elems)