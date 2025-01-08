import math
side1 = 3.0
side2 = 4.0

def circumference_triangle(side1, side2):
    return math.sqrt(math.pow(side1, 2) + math.pow(side2, 2)) + side1 + side2

print(circumference_triangle(side1, side2))

f = lambda: math.sqrt(math.pow(side1, 2) + math.pow(side2, 2)) + side1 + side2
print(f())