import math


def area(a, b):
    def area_square_figure(a, b):
        return (a * b) / 2

    def area_half_circle_figure(a):
        r = a / 2
        return math.pi * math.pow(r, 2)

    return area_square_figure(a, b) + area_half_circle_figure(a)


def circumference(a, b):
    def circumference_square_figure(a, b):
        return b + math.sqrt(math.pow(a, 2) + math.pow(b, 2))

    def circumference_half_circle_figure(a):
        return (2 * math.pi * a) / 2

    return circumference_half_circle_figure(a) + circumference_square_figure(a, b)


a = float(input("Gitt en vilkårlig figur.\nSkriv inn lengden på den ene siden: "))
b = float(input("Skriv inn lengden på den andre siden: "))
print(f"Areal av figuren er {area(a, b)}\nOmkrets: {circumference(a, b)}")
