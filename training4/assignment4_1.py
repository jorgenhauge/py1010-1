import numpy as np
import matplotlib.pyplot as plt
import pathlib

p = pathlib.Path(__file__).with_name("temp_skien_oo_plotting.pdf")
filename = p.absolute()

months = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])  # [month no]
temperatures_c = np.array([-3, -2, 2, 7, 11, 15, 17, 16, 12, 6, 2, -3])  # [C]
temperatures_f = temperatures_c * (9 / 5) + 32 # [F]

fig = plt.figure()  # Make a figure object with name fig.
ax = fig.subplots()  # Make an axes object with name ax.
plt.xlabel("Month number")
plt.ylabel("Value")
plt.xticks(months)
plt.grid()
ax.plot(
    months, temperatures_c, "*-b", label="temp C vs month"
)  # Use ax.plot() to plot.
ax.plot(
    months, temperatures_f, "*-g", label="temp F vs month"
)  # Use ax.plot() to plot.
ax.axhline(
    y=np.nanmean(temperatures_c),
    label="Mean value of temp C",
    color="r",
    linestyle="--",
)
ax.axhline(
    y=np.nanmean(temperatures_f),
    label="Mean value of temp F",
    color="c",
    linestyle="--",
)
ax.autoscale(axis="y")

plt.legend()
plt.savefig(filename)
plt.show()  # Show the plot with plt.show()
