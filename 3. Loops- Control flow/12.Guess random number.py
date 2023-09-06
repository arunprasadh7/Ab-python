#Guess a number between 1 and 10

import random
n = random.randint(1,10)
guess = 0
#print(n)
while guess != n:
    guess = int(input("Enter a number : "))
    if guess > n:
        print("Number is lower than entered number.")
    elif guess < n:
        print("Number is higher than entered number.")
    else:
        print("Congrats ...You have guessed the right number!!!")