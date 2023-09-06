# Display multiplication table using for loop

n = int(input("Enter the number : "))

for i in range(1,11):
    m = n * i
    print(n,'X',i,'=',m)
