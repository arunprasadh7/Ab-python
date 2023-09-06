# Arithmetic progression - for loop

a = int(input("Enter starting value : "))
d = int(input("Enter the difference value : "))
n = int(input("Enter the number of terms : "))

for i in range(a,n*d+a,d):
    print(i,end=" ")