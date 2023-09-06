# Check if student has passed or failed by taking marks in 3 subjects

math = int(input("Enter math mark : "))
physics = int(input("Enter physics mark : "))
chemistry = int(input("Enter chemistry mark : "))

# average = (m + p + c) / 3

if math >= 45 and physics >= 45 and chemistry >= 45:
    print("Pass")
else:
    print("Fail")
