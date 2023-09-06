#challenge - Display data in a given format(25 letters)

name = input("Enter product name : ")
price = input("Enter product price : ")
total_length = len(name) + len(price)
print(total_length)
max = 25
dots = '.' * (max-total_length)
print(name+dots+price)

