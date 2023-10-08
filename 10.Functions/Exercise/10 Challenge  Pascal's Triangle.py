# 10 Challenge  Pascal's Triangle

def pascals(n=1):
	r = [1]

	for i in range(n):
		print(r)
		tr = [0] + r 
		r = r + [0]
		r = [x+y for x,y in zip(r,tr)]

pascals(6)