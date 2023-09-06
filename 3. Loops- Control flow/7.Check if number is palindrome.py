# To check if number is palindrome
#Palindrome - reverse of a number is same as the original number (eg. 1221 -1221)

n = int(input("Enter the number : "))
print("Given number is",n)
m = n
rev = 0

while n > 0:
    r = n%10
    n = n//10
    rev = rev * 10 + r


print("Reverse of the number is",rev)
print(n)
if m == rev :
    print("Given number is a Palindrome")
else:
    print("Number not a Palindrome")