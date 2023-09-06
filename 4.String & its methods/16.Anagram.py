#Check if the given string is Anagram
#Anagram - if two strings contain same characters (even in random order)

s1 = input("Enter first string : ")
s2 = input("Enter second string : ")

if len(s1) == len(s1):
    if sorted(s1) == sorted(s2):
        print("Strings are Anagram")
    else:
        print("Not anagram")
print("Bye")