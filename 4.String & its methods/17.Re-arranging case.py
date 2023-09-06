#Re-arrange the given string to lowercase and then uppercase

s1 = input("Enter the string : ")
lower = []
upper = []
special =[]

for i in s1:
    if i.islower():
        lower.append(i)
    elif i.isupper():
        upper.append(i)
    else:
        pass

print(f"Lower case :{lower}\nUpper case :,{upper}")
joining = ''
print("Rearranged string is :",joining.join(lower)+joining.join(upper))