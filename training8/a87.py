import numpy as np

def my_linspace(start, stop):
    assert start < stop
    step = (stop - start) / 50
    while stop > start:
        yield start
        start += step

print(list(my_linspace(1, 7)))
print(np.linspace(1, 7, 50))

