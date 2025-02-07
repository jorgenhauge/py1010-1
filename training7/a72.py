social_security_number = input("Input social security number(11 digits): ")
assert len(str(social_security_number)) == 11

gender_digit: int = int(social_security_number[8])
if gender_digit % 2 == 0:
    print(f"{social_security_number} is bound to a woman")
else:
    print(f"{social_security_number} is bound to a man")
