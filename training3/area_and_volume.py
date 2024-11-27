import math


def main():
    choice: str = input(
        "Calculate area and volume of a figure, choose figure: [s=sphere or t=right triangle]: "
    )
    if choice == "s":
        radius: float = float(input("Please input radius of sphere: "))
        area: float = 4 * math.pi * math.pow(radius, 2)
        volume: float = 4 / 3 * math.pi * math.pow(radius, 3)
        print(f"Area: {area}, Volume: {volume} for sphere with radius: {radius}")
    elif choice == "t":
        catet: float = float(input("Please input right triangle catet: "))
        hypotenuse: float = float(input("Please input right triangle hypotenuse: "))
        other_catet: float = math.sqrt(math.pow(hypotenuse, 2) - math.pow(catet, 2))
        area: float = catet * other_catet / 2
        circumference: float = catet + other_catet + hypotenuse
        alpha: float = math.atan(other_catet / catet)
        theta: float = math.atan(catet / other_catet)
        assert math.radians(90) + alpha + theta == math.radians(180)
        print(
            f"Other catet size: {other_catet}, Area: {area}, circumference: {circumference}, alpha(radians/degrees): {alpha}/{math.degrees(alpha)}, theta(radians/degrees): {theta}/{math.degrees(theta)}"
        )
    else:
        raise ValueError(
            "No, or invalid argument provided. Choices: [s=sphere or t=triange]"
        )


if __name__ == "__main__":
    main()
