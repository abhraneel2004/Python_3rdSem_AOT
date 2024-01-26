
def allprime(l):
	for i in l:
		c=0
		if i<=1:
			return False
		for j in range(2, int(i**0.5)):
			if i%j==0:
				c+=1
				return False
		if c>0 and c!=2:
			return False
		else:
			return True

l1 = eval(input("Enter list 1: "))
print(allprime(l1))
