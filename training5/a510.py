import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x ** 2 + 3

def g(x):
    return 3 * x + 1

x = np.linspace(-2, 3, 100)

plt.plot(x, f(x), "blue", label="f(x)")  # line
plt.plot(x, g(x), "green", label="g(x)") # line
plt.grid()
plt.legend()
plt.show()