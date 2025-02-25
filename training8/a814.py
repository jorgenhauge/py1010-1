x = 10
counter = 0

while True:
    x = x / 2
    if x >= 0.04:
        counter += 1
    else:
        break
print(f"X: {x}, counter: {counter}")
