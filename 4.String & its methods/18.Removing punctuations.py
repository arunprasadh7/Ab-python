# Remove punctuations from the given string

s1 = input("Enter the string : ")
s2 = []
for i in s1:
    if i.isalnum():
        s2.append(i)
print(s2)
s3 = ''
print("Modified string is :",s3.join(s2))