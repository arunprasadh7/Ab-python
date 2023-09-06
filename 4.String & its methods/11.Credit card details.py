#Display credit card number

card_number = input("Enter the 16 digit number : ")
last4_number = card_number[:-5:-1]
#print(last4_number)
print('*'*4,'*'*4,'*'*4,last4_number)