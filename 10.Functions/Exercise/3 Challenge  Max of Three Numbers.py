# 3 Challenge  Max of Three Numbers

def max3(x,y,z):
	if x > y and x>z:
		return x 
	elif y >x and y>z:
		return y 
	else:
		return z

print('The max number is :',max3(10,20,30))