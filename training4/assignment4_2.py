import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(1, 5, 5).astype(int)
y = x
z = np.sqrt(x)
plt.plot(x, y, "*-r", label="x vs y")
plt.plot(x, z, "o-b", label="sqrt(x)")
plt.xlabel("x[s]")
plt.ylabel("[m]")
plt.grid()
plt.legend()
plt.show()
f = plt.figure()
f.set_figheight(val=9 / 2.54)
f.set_figwidth(val=12 / 2.54)

f.savefig("plot1.pdf")