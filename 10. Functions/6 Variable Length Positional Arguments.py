#8. Variable Length Positional Arguments
'''
syntax:
def fun1(*args):
  print(args)
'''

def fun1(*nums):
  print(type(nums), nums)

fun1()
fun1(10)
fun1(10,20)
fun1(10,20,30)
fun1(10,'Hello', 24.57, True)

def fun2(a, b, *args):
    print(a,b, args)
  
fun2(2,3,4,5,6,7)

#type 2

def fun3(*args, a, b):
   print(a,b,args)
  
fun3(11,22,33,44,a=55, b=66)