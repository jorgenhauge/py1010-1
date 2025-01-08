import numpy as np

S = np.array([1.05, 1.30, 1.10, 0.94, 1.21])

def speed(distance: float, t: float = 2.0):
    return distance / t

def mean_speed(S: np.array, t: float = 2.0):
    return np.mean(np.array([speed(e, t) for e in S]))

print(f"Mean speed: {mean_speed(S)} m/s")