temperature: float = float(input("Please provide temperature of water to get the phase of the water: "))
if temperature <= 0:
    print("Phase of water is ICE")
if 0 < temperature <= 99:
    print("Phase of water is FLUID")
if temperature >= 100:
    print("Phase of water is GAS")
