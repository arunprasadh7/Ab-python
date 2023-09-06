#Find day, month and year from user enterd date(string)

s1 = input("Enter the date (dd/mm/yyyy) : ")
s2 = s1.split('/')
#print(s2)
day = s2[0]
month = s2[1]
year = s2[2]

print("Day :",day)
print("Month :",month)
print("Year :",year)