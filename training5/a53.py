def convert_currency(euro: float):
    nok: float = euro * 10.42
    dollar: float = euro * 1.19
    return nok, dollar

amount_euro: float = 50

nok, dollar = convert_currency(amount_euro)
print(f"\N{euro sign}: {amount_euro} is: NOK: {nok}, \N{dollar sign}: {dollar}")