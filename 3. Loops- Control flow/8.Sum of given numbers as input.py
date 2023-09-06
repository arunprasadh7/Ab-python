#Find sum of given numbers as input

num_of_numbers = int(input("How many numbers would you like to enter ?: "))
count = 0
sum = 0

while count< num_of_numbers:
    n = int(input("Enter the number : "))
    sum+=n
    count+=1

print("Sum of given numbers is",sum)