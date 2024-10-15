import math


def area(a, b):
    return (math.pi * math.pow(a, 2)) / 2 + (a * b) / 2


def circumference(a, b):
    return 2 * math.pi * a + b + math.sqrt(math.pow(a, 2) + math.pow(b, 2))


a = float(input("Gitt en vilkårlig figur.\nSkriv inn lengden på den ene siden: "))
b = float(input("Skriv inn lengden på den andre siden: "))
print(f"Areal av figuren er {area(a, b)}\nOmkrets: {circumference(a, b)}")
