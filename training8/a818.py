import numpy as np

x = np.linspace(3, 22, 20)
index = 0

while True:
    if np.sum(x[0:index]) > np.sum(x[index+1:]):
        print(f"At index: {index} the sum(left hand side): {np.sum(x[0:index])} of x is larger than the sum(right hand side): {np.sum(x[index+1:])}")
        break
    else:
        index += 1
