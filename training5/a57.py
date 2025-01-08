import math

def kinetic_energy(mass: float, velocity: float):
    ek = 1/2 * mass * math.pow(velocity, 2)
    return ek

mass=80.0
velocity=12.0

ek = kinetic_energy(mass=mass, velocity=velocity)
print(f"Kinetic energy with mass: {mass}, velocity: {velocity} is: {ek} kg m/s")