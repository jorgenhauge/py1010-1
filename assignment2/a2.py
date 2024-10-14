import math

antall_elever = int(input("Skriv inn antall elever: "))
# math.ceil() returns an int
print(
    f"Gitt en elev spiser 1/4 pizza, må det kjøpes inn: {math.ceil(antall_elever * 0.25)} pizza"
)
