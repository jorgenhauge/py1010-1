names = ["Eli", "Ola", "Ali", "Ela"]
phones = [9423234, 9223001, 4756001, 9592676]

name = input(f"Please provide a name from choices '{names}' to get the phone number for the name: ")
index = names.index(name)
print(f"{name}'s phone number is: {phones[index]}")