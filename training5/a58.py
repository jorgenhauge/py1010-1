import math


def potential_energy_height(mass: float, ep: float, G: float = 9.81):
    height = ep / mass * G
    return height

mass = 0.48
ep = 34.37

height = potential_energy_height(mass=mass, ep=ep, G=1.6)
print(f"Height above sea level: {height} m, with mass: {mass} and potential energy: {ep}")