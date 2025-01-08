import numpy as np

def calculate_values(a: np.array):
    return len(a), a.max()

a = np.array([1.2, 5.9, -3.1, 7.9, 0.6])

print(calculate_values(a))