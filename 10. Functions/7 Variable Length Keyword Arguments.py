#9. Variable Length Keyword Arguments

# syntax
def fun2(**kwargs): #stores as keyword args as dict
    print(kwargs)

fun2(name='Arun', rollno = 6, add='TamilNadu')


#Mixed args
def fun3(a,b,*args, **kwargs): #a, b must be positional only
    print(a, b, args, kwargs)