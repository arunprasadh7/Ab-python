# Checking whether the string is a palindrome

s1 = input("Enter the string : ")
s2 = s1[::-1]
#print(s2)
if s1 == s2:
    print("Given string is a Palindrome!!")
else:
    print("Not a Palindrome.")
