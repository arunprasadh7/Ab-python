# 12. Recursive Function - a funtion calling itself is called as recursive function eg factorial 

# fact(n) = n* (n-1)
#5 = 5 * 4 * 3 * 2 * 1

def fact(n):
	if n == 0:
		return 1
	else:
		return n*fact(n-1)

print(fact(5))

