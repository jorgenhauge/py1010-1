import math

print(r"Please type the x and y coordinates multiple times. When you're done please type 'Done':")
distances: float = 0
while True:
    xd = input("Skriv inn x-koordinaten for startpunkt: ")
    yd = input("Skriv inn y-koordinaten for startpunkt: ")
    if xd == "Done" and yd == "Done":
        break
    else:
        distances += math.sqrt(math.pow(abs(float(xd)), 2) + math.pow(abs(float(yd)), 2))

print(f"Covered distance is: {distances}")
