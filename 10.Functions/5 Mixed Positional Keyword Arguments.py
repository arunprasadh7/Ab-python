#6. Mixed Positional Keyword Arguments

def add(a,b,c,d,e,f):
    print(a, b, c, d, e, f)
    return a+b+c+d+e+f

r = add(2, 5, 7, 4, 8, 9)
print(r)

k = add(f=9, e=8, a=2, c=7, b=5, d=4)
print(k)

#only positional args before /

def add3(a,b,/): #can take only pos args 
    return a+b

print(add3(2,5))

#only keyword args after *

def add4(*,a,b):
    return a+b

print(add4(b=5,a=6))



def add1(a,b, /, c,d,e,f): #contains both positional and keyword args
    print(a, b, c, d, e, f)
    return a+b+c+d+e+f


pk = add1(2, 5, f=9, e=8, c=7, d=4)
print(pk)


def add2(a, b, /, c, d, *, e, f): #anything before / must be positional, anything after * must be keyword args
    print(a, b, c, d, e, f)
    return a+b+c+d+e+f

# pk2 = add2(2,5,6,7,8,9) #8,9 must be specified as keyword args
pk2 = add2(2,5,6,7,e=8,f=9)
print(pk2)
