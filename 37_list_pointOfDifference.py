def pointdiffer(l1,l2,n):
	for i in range(n):
		if not l1[i]==l2[i]:
			return i
	return 'Same'

n = int(input("Enter the no. of elements: "))

l1,l2 = [],[]

print("List 1: ")
for i in range(n):
	x = int(input("Enter the element: "))
	l1.append(x)

print("List 2: ")
for i in range(n):
	x = int(input("Enter the element: "))
	l2.append(x)

print(pointdiffer(l1,l2,n))	

