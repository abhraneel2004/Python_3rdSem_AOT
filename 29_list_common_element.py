def common(l1,l2):
	l1,l2 = set(l1), set(l2)
	return list(l1.intersection(l2))
	
l1 = eval(input("Enter list 1: "))
l2 = eval(input("Enter list 2: "))
l = common(l1,l2)
if(l):
	print("Common Elements: ",l)
else:
	print("Nothing in common")
