# while loop example 2
# to execute as long the condition is true

n = int(input("Enter the number : "))

while n>0:
    r = n % 10 # gives remainder
    n = n // 10 # gives closest whole number
    print(r)