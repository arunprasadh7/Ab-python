                    #Dictionary looping

d1 = {101:'Production',102:'Accounts',103:'Sales & Marketing',104:'Inventory'}

for x in d1:        # prints only key
    print(x)

for x in d1:        # prints key & value
    print(x,d1[x])

#get(key, value)
for x in d1:
    print(x,d1.get(x))

print(d1[104])
#print(d1[106]) - throws error as the value is out of range

print(d1.get(102))
print(d1.get(106))  #does not throw error if out of range value is given
print(d1.get(106,'Unknown department')) #for out of range value,prints default msg

#keys() - prints the keys for the dict
print(d1.keys())

for k in d1.keys():
    print(k,d1[k])

#values() - prints the values from the dict
print(d1.values())

for i in d1.values():
    print(i)

#items() - prints both key & value
print(d1.items())

for x,y in d1.items():
    print(x,y)



