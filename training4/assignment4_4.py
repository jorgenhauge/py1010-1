# Firma A: 1204, Firma B: 1119, Firma C: 998
import numpy as np
import matplotlib.pyplot as plt

company_names = np.array(["Firma A", "Firma B", "Firma C"])
sold_units = np.array([1204, 1119, 998])

plt.barh(company_names, sold_units)
plt.ylabel("Company name")
plt.xlabel("Sold units")
plt.show()