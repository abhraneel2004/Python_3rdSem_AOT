def common(l1,l2):
	l1,l2 = set(l1), set(l2)
	if len(l1.intersection(l2))==0:
		return False
	return True
	
l1 = eval(input("Enter list 1: "))
l2 = eval(input("Enter list 2: "))
print(common(l1,l2))

