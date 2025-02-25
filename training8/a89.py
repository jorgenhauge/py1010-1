import math

"""
En historie lyder som følger: Vismannen Sissa i India oppfant sjakk rundt aar 600. Herskeren
ble begeistret og ville gi vismannen en gave. Han ba om ett hvetekorn i den første ruta paa
sjakkbrettet, to korn i neste, fire i den tredje, osv. Ikke noe problem, sa herskeren, som
neppe hadde regnet paa det, men det skal vi gjøre.
Sjakkbrettet har 64 ruter. Vi antar at et hvetekorn veier 50 mg.
Lag et program som svarer paa følgende spørsm ̊al:
• Hvor mange korn har Sissa ønsket seg? Beregn svaret med en for-løkke.
• Hva er vekten i tonn av alle kornene han ønsket seg? Anta at hvert menneske paa jorda
ble bedt om  ̊a hjelpe herskeren med aa oppfylle ønsket. Hvor mye (i kg) blir det paa
hver? Anta da at det paa 600-tallet var 200 millioner mennesker paa jorda.
"""

grain: int = 0

for i in range(64 + 1):
    grain += int(math.pow(2, i))
print(f"{grain:_}")
print(
    f"""Weight (kg): {grain * 0.050} and contribution from one 
    person on the planet at 600 AD (200 million people): {grain * 0.050 / 200_000_000} kg/person"""
)
