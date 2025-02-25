import numpy as np
import matplotlib.pyplot as plt

arr = np.array([100 / np.pow(10, i) for i in range(0, 20)])
print(f"{arr}, len(arr): {len(arr)}, sum(arr): {np.sum(arr)}")

x = np.arange(0, 20)

print(len(x), len(arr))

plt.xlabel("x")
plt.ylabel("y/f(x)")
plt.plot(x, arr, "-r", label="x vs y")
plt.show()