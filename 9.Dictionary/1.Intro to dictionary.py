#Dictionary - key value pairs/ entry/ items
#value - can take any data type for value
#key - can take only immutable data type (except set & list)

d1 = {'abacus':'a calculator','bachelor' :'unmarried person','cable':'strong rope'}
#       key   : value
print(d1['abacus'])

#dict of roll number & name
#key = roll number
#value = name
d2 = {101:'john',102:'smith',103:'Arun',104:'Prasadh' }
d2[102] = 'mathew'
print(d2)

#adding new elements to dict
d2[105] = 'added element'
print(d2)
d2[106] = 'Arc warden'
print(d2)

#deleting elements from the dic
del d2[106]
print(d2)

#loops in dict

for i in d2:
    print(i)    #prints only the key

for i in d2:
    print(i,d2[i])  #prints key & value

#sample dictionaries
d3 = {'apple':'red','grapes':'gree','mango':'yellow'}
d4 = {'name':'arun','age':26,'gender':'male','ph no':8870127912}
