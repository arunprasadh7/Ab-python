#Convert roman numerals to decimal values

roman_values = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}

roman_numeral = "MCMXCIV"  # Example: 1994

decimal = 0
prev_value = 0

for symbol in roman_numeral[::-1]:
    value = roman_values[symbol]

    if value < prev_value:
        decimal -= value
    else:
        decimal += value

    prev_value = value

print(f"The decimal value of {roman_numeral} is {decimal}")
