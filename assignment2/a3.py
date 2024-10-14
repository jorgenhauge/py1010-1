import numpy as np

v_grad = float(input("Skriv inn gradtallet: "))
v_rad = v_grad * np.pi / 180
print(f"Antall grader {v_grad} er: {v_rad} radianer")
