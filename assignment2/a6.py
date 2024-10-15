import numpy as np
import matplotlib.pyplot as plt


def myfunc(x):
    return np.pow(-x, 2) - 5


x = np.linspace(-10, 10, 200)

plt.plot(x, myfunc(x), "blue")  # line
plt.ylabel("f(x) = -x^2 - 5")
plt.xlabel("x")
plt.show()
