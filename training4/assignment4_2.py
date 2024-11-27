import numpy as np
import matplotlib.pyplot as plt
import pathlib

p = pathlib.Path()

x = np.linspace(1, 5, 5).astype(int)
y = x
z = np.sqrt(x)
plt.plot(x, y, "*-r", label="x vs y")
plt.plot(x, z, "o-b", label="sqrt(x)")
plt.xlabel("x[s]")
plt.ylabel("[m]")
plt.grid()
plt.legend()
plt.savefig((p.cwd() / "plot1.pdf").as_posix())
plt.show()
fig = plt.gcf()
fig.set_figheight(val=9 / 2.54)
fig.set_figwidth(val=12 / 2.54)
