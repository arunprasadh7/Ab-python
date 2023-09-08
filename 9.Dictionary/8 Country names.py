#Country names

countries = {}

for i in range(5):
  name = input('Enter country name: ')
  first = name[0].upper()
  if first not in countries:
    countries[first] = [name]
  else:
    countries[first].append(name)

print(countries)