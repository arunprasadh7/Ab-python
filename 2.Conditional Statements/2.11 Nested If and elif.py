# program to demonstrate nested if and else if
# using age of three people find out whos the eldest

a = int(input("Enter first age, a : "))
b = int(input("Enter second age, b: "))
c = int(input("Enter third age, c: "))

if a > b and a > c:
    print("A is eldest")
elif b > c:
    print("B is eldest")
else:
    print("C is greatest")
