speed: float = float(input("Please input you speed(km/h): "))

limit: float = 60.0

if 60.0 < speed <= 65.0:
    print(f"You're fine is 800 NOKs")

if limit + 5.0 < speed <= limit + 10.0:
    print(f"You're fine is 2100 NOKs")

if limit + 10.0 < speed <= limit + 15.0:
    print(f"You're fine is 3800 NOKs")

if limit + 15.0 < speed <= limit + 20.0:
    print(f"You're fine is 5500 NOKs")

if limit + 20.0 < speed <= limit + 25.0:
    print(f"You're fine is 8500 NOKs")

else:
    print("You are driving way to fast!")
