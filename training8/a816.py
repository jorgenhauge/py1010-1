x: float = 0


def f(x: float):
    return 2 * x - 3


def g(x: float):
    return -x + 5


while True:
    if f(x=x) < g(x=x):
        x += 0.01
    else:
        print(f"When f(x) > g(x), x is then: {x:.3f}")
        break