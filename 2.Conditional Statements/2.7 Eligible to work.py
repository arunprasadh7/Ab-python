# Check if a person is eligible to work

age = int(input("Enter your age : "))

if age >= 18 and age<= 60:
    print("Eligible to work")
elif age >60 :
    print("Enjoy your retirement")
else:
    print("Not eligible")
