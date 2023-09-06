# display multiplication table for the given number using loops

n = int(input("Enter the number : "))

count = 1
while count <=10:
    t= n * count
    print(n,"X",count,"=",t)
    count = count+1
print("Bye!")