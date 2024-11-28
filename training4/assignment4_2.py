import numpy as np
import matplotlib.pyplot as plt
import pathlib

p = pathlib.Path(__file__).with_name("plot1.pdf")
filename = p.absolute()

x = np.linspace(1, 5, 5).astype(int)
y = x
z = np.sqrt(x)
fig, axs = plt.subplots(2)
plt.xlabel("x[s]")
plt.ylabel("[m]")
axs[0].plot(x, y, "*-r", label="x vs y")
axs[0].grid()
axs[0].legend()
axs[1].plot(x, z, "o-b", label="sqrt(x)")
axs[1].grid()
axs[1].legend()
plt.savefig(filename)
plt.show()
