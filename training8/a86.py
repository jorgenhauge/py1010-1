"""
Bruk numpys linspace-funksjon til  ̊a generere 20 x-koordinater p ̊a intervallet [0, π]. Opprett
funksjonen f (x) = sin(x). Lag s ̊a en for-løkke som fortløpende skriver x-verdiene og de
tilhørende funksjonsverdiene til skjerm med passende tekst.
"""
import numpy as np

x_array = np.linspace(0, np.pi)

for x in x_array:
    print(f"x: {x}, f(x): {np.sin(x)}")