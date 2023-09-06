#For loop - Fibonacci series

a = 0
b = 1
n = int(input("Enter number of terms : "))

for i in range(n):
    print(a)
    c = a + b
    a = b
    b = c
#print(c, end=" ")