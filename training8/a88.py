import numpy as np


# def my_linspace(start, stop):
#     assert start < stop
#     increment = 0.1
#     while stop > start:
#         yield start
#         start += increment

# for x in my_linspace(-2, 2):
#     y = x**x + 1
#     print(f"x: {x}, f(x): {y}")

x_range = np.arange(-2, 2, 0.1)

for x in x_range:
    y = np.power(x, 2) + 1
    print(f"x: {x}, f(x): {y}")
print(
    f"MAX: {x_range.max()} -> index pos: {x_range.argmax()}, MIN: {x_range.max()} -> index pos: {x_range.argmin()}"
)
