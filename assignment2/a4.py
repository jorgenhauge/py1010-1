import sys

data: dict = {
    "Norge": ["Oslo", 0.634],
    "England": ["London", 8.982],
    "Frankrike": ["Paris", 2.161],
    "Italia": ["Roma", 2.873],
}

landsnavn = input(f"Skriv inn et land fra dette utvalget: {tuple(data.keys())} ")
try:
    hovedstad, innbyggere = data.get(landsnavn)[0], data.get(landsnavn)[1]
except IndexError as e:
    print(f"Finner ikke: {landsnavn} som du skrev inn, feil: {e}")
    sys.exit(1)
print(
    f"{hovedstad} er hovedstaden i {landsnavn} og det er {innbyggere} mill. innbyggere i {hovedstad}"
)
