#to find the sum of digits in a number

n = int(input("Enter the number: "))
sum = 0

while n>0:
    r = n % 10
    n = n//10
    sum += r
print("The sum of the numbers is",sum)
print("Bye")