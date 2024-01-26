def unique(l):
	l = set(l)
	return list(l)
	
l = []
s = int(input("Enter the number of elements: "))
for i in range(s):
	x = int(input("Enter element: "))
	l.append(x)
	
print(unique(l))
