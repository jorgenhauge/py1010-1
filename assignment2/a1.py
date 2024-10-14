from datetime import datetime
dette_aar = datetime.now().year

alder = int(input("Hvilket år er du født? "))
print(f"Du ble/blir: {dette_aar - alder} gammel i år {dette_aar}")
