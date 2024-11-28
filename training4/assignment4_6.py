# Firma A: 1204, Firma B: 1119, Firma C: 998
import numpy as np
import matplotlib.pyplot as plt

company_names = np.array(["Firma A", "Firma B", "Firma C"])
sold_units = np.array([1204, 1119, 998])
explode = (0, 0.1, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
fig1, ax1 = plt.subplots()

plt.pie(
    sold_units, explode=explode, labels=company_names, autopct="%1.1f%%", shadow=True
)
plt.show()
