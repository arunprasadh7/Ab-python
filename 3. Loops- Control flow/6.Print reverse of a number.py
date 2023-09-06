# To print reverse of a given number

n = int(input("Enter the number: "))
revert = 0

while n > 0:
    remainder = n % 10
    n = n // 10
    revert = revert * 10 + remainder
    #print(remainder)
print("Reverse of the number is",rev)
print("Bye")