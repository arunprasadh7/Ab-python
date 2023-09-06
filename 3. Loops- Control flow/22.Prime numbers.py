# Print Prime numbers between 1 - 100

#n = int(input("Enter the number : "))
for n in range(1,101):
    count = 0

    for i in range(1,101):
        if n % i == 0:
            count+=1

    if count == 2:
        print(n)