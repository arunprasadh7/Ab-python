#Local vs global 
# global variable must be declared before the function call
# local variable are declared within the function

g = 10 #global variable

def fun1(a,b):
	c = a+b #local variable
	print('local',c)
	print('global',g)

fun1(4,8)


def fun2():
	print(g*2)

fun2()


# when global and local variables have similar names priority is given to local variable
g = 20
def fun3():
	g = 5
	print(g)

fun3()
print('global',g)


# A function cannot simply modify global variables, it can only access them
g = 50
def fun4():
	global g
	g = g + 5
	print(g)

fun4()
print(g)


#Locals and globals function

a, b, c, d = 11, 22, 33, 44

def locals_fun():
	x,y,z = 1,2,3
	print(locals())	#locals returns all local variables and their associated values as dict

locals_fun()

def locals_fun1(a=10, b=25): #default args
	x,y,z = 30,40,50
	print(locals())	#includes all variables with default ones

locals_fun1()

print(globals()) #gives all global varibles and global built in functions across python