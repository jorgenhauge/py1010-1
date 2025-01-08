import math

def calculate_catet(catet1, hypotenuse):
    catet2 = math.sqrt(math.pow(hypotenuse, 2) - math.pow(catet1, 2))
    return catet2

print(calculate_catet(4, 5))