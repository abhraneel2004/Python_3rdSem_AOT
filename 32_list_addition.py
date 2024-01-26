n = int(input("Enter the no. of elements: "))
l1,l2 = [],[]
l3 = []

print("List 1: ")
for i in range(n):
	x = int(input("Enter the element: "))
	l1.append(x)

print("List 2: ")
for i in range(n):
	x = int(input("Enter the element: "))
	l2.append(x)
	
for i in range(n):
	l3.append(l1[i]+l2[i])

print(l3)
