#Challenge - birthday of a person

birthday = {
    "Alice": "January 15, 1990",
    "Bob": "March 22, 1985",
    "Charlie": "July 10, 1995",
    "David": "November 5, 1982",
    "Eve": "May 18, 1998"
}
name = input('Enter name : ')

if name in birthday.keys():
  print(f'Date of Birth : {birthday[name]}')
else:
  print(f'No records found for {name}')