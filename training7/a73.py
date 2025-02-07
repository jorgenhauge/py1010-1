x, y = (
    float(input("Input x for point in plane: ")),
    float(input("Input y for point in plane: ")),
)

if x > 0 and y > 0:
    print(f"{x}, {y} is in Quadrant I")

if x < 0 and y > 0:
    print(f"{x}, {y} is in Quadrant II.")

if x < 0 and y < 0:
    print(f"{x}, {y} is in Quadrant III")
