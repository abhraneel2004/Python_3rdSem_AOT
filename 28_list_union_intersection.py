def union1(l1,l2):
	l1 = set(l1)
	l2 = set(l2)
	
	return list(l1.union(l2))
	
def intersection1(l1,l2):
	l1 = set(l1)
	l2 = set(l2)
	return list(l1.intersection(l2))
	
l1 = eval(input("Enter list 1: "))
l2 = eval(input("Enter list 2: "))
print(union1(l1,l2))
print(intersection1(l1,l2))
