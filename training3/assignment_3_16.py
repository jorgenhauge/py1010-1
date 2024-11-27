import math

print(
    "Given: ax2 + bx + c = 0, and that b^ - 4ac >= 0 which tells that this equation has zero point. "
    "Based on your input for a, b and c determine if there is a real solution to the equation"
)
while True:
    a = float(input("Please input 'a': "))
    b = float(input("Please input 'b': "))
    c = float(input("Please input 'c': "))
    break

if math.pow(b, 2) - 4 * a * c >= 0:
    print(f"a, b, c: {a, b, c} has solution(s)")
else:
    print(f"a, b, c: {a, b, c} has no solution(s)")
