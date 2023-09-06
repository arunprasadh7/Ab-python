# Check for voting age

age = int(input("Enter your age : "))

if age < 18:
    print("Not eligible")

elif age == 18:
    print("You have to wait till end of year")

else:
    print("Eligible")
