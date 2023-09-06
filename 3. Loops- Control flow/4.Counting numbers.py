# Counting the number of digits in a number

n =int(input("Enter the number : "))
count = 0
#print(len(n))

while n >0:
    n = n // 10
    count+=1

print(count)
print("Bye")

