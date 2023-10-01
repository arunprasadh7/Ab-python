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

'''
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
'''

#method 2

number = input('Enter the roman number: ').upper()
decimal = 0

i = 0
while i < len(number):
    if (i+1) < len(number) and roman_values[number[i]] < roman_values[number[i+1]]:
        decimal += roman_values[number[i+1]] - roman_values[number[i]]
        i += 2
    
    else:
        decimal += roman_values[number[i]]
        i += 1

print(f'The decimal value of \'{number}\' is {decimal}.')