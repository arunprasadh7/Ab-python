# How to write a function
#parameters - input to a function

'''
def fun_name(p1,p2,p3): # formal parameters
    statement1
    statement2
    statement3
    return result

#calling a function
fun_name(ap1,ap2, ap3) # actual parameters
return value = fun_name(ap1, ap2, ap3)

'''
#function for adding three numbers

def add_number(x,y,z):
    result = x + y + z
    return result

print(add_number(5,5,5))

r = add_number(10,20,30)
print(r)