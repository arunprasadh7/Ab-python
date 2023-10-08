#18.Challenge  Difference Between Two Numbers
# take 2 numbers and check if the max difference between them is 5

def diff(x,y):
	if abs(x-y) <= 5:
		return True
	else:
		return False

print(diff(8,6))
print(diff(10,50))