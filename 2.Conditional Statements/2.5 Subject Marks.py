# Check if marks of subject are within 0 - 100

mark = int(input("Enter the mark : "))

if mark >= 0 and mark <= 100:
    print("Marks are within the specified range")
else:
    print("Out of range")
