string: str = "Nedre grense for karakter E er 40 poeng."
for s in string.split():
    if s == "40":
        print(int(s))