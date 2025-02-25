import math

x: float = 0


def f(x: float):
    return math.exp(x) - 3


def g(x: float):
    return -x


while True:
    if not math.isclose(f(x=x), g(x=x), abs_tol = 0.4):
        x += 0.01
    else:
        print(f"When f(x) == g(x), x is then: {x:.3f}")
        break
