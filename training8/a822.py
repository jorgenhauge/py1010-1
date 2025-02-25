import time
import numpy as np

start = time.time()
arr = np.arange(start=1, stop=200000, step=2)
end = time.time()

print(f"Delta create time: {end - start} s for arr: {arr}")
