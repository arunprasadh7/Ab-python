#For loop - Factorial of a given number

n = int(input("Enter the number : "))
fact = 1
for count in range(1,n+1):
    fact = fact * count
    #print(fact)
print("Factorial of",n,"=",fact)
