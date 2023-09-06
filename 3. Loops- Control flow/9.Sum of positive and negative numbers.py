#Find the sum of positive and negative numbers

num_of_nos = int(input("How many numbers would you like to enter ? "))
count = 0
p_sum = 0
n_sum = 0

while count<num_of_nos:
    n = int(input("Enter the number : "))
    if n>0:
        p_sum+=n
    else:
        n_sum+=n
    count+=1

print("Sum of positive numbers is",p_sum)
print("Sum of negative numbers is",n_sum)
