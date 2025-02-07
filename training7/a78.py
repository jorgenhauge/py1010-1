import numpy as np
import matplotlib.pyplot as plt

x_coor = float(input("Input a x coordinate for f(x) = sin(x): "))

y = np.sin(x_coor)
if x_coor < 0 or x_coor > 4 * np.pi:
    print("x-koordinaten ligger utenfor intervallet")
if 0 <= x_coor <= 4 * np.pi:
    if y > 0.5:
        print("(x) er større enn 0.5")
    if y <= 0.5:
        print("(x) er mindre eller lik 0.5")

# x = np.linspace(0, 4*np.pi)
# plt.xlabel("x")
# plt.ylabel("y/f(x)")
# plt.plot(x, y, "-r", label="x vs y")
# plt.show()
