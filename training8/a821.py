K = 0.01
runs = 0
x = 2


def f(x: float):
    return x**2 + 1


def f_derived(x: float):
    return 2 * x


while (x := x - K * f_derived(x)) >= 0.0001:
    runs += 1
    if runs >= 10000:
        print(f"Loop ended at: {runs}")
        break
    print(f"X-optimal: {x}, runs: {runs}")
