#Find maximum numbers from given number

no_of_nos = int(input("How many numbers would you like to enter? "))
count = 0
# max = 0  #this method wont work if the number is negative
max = int(input("Enter a number : "))
#while  count < no_of_nos:
while  count < no_of_nos -1:
    n = int(input("Enter the number : "))
    if n > max:
        max = n
    count+=1
print("The maximum number is",max)