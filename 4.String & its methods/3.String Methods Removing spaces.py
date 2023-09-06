            #Removing spaces
#Alignment
#ljust , rjust ,center
#s.ljust(width[,fill]) - left justified
#s.rjust(width[,fill]) - right justified
#s.center(width[,fill]) - center align

s = 'python'

print(s.ljust(10,'-'))
print(s.rjust(10,'-'))
print(s.center(10,'-'))
print("")

#Strip method - by default removes spaces, can remove mentioned character
#s.strip([chars])
#s.lstrip([chars])
#s.rstrip([chars])

s1 = '***python***'
print(s1.lstrip('*'))
print(s1.rstrip('*'))
print(s1.strip('*'))
print("")

s2 = '...   +++aaapython'
print(s2.strip('. +')) #can give multiple chars to remove