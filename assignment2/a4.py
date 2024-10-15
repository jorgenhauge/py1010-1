data: dict = {
    "Norge": ["Oslo", 0.634],
    "England": ["London", 8.982],
    "Frankrike": ["Paris", 2.161],
    "Italia": ["Roma", 2.873],
}

landsnavn = input(f"Skriv inn et land gitt: {tuple(data.keys())} ")
if landsnavn not in data:
    print(
        f"Finner ikke: '{landsnavn}' i {tuple(data.keys())}.\nLa oss fylle inn detaljer om {landsnavn}"
    )
    hovedstad = input(f"Skriv inn hovedstad i {landsnavn}: ")
    innbyggertall = float(
        input(f"Skriv inn antall innbyggere i {hovedstad} i millioner: ")
    )
    data[landsnavn] = [hovedstad, innbyggertall]
    print(data)
else:
    hovedstad, innbyggere = data.get(landsnavn)[0], data.get(landsnavn)[1]
    print(
        f"{hovedstad} er hovedstaden i {landsnavn} og det er {innbyggere} mill. innbyggere i {hovedstad}"
    )
