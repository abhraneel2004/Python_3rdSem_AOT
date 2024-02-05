n = int(input("Enter the no. of elements: "))
l1,l2 = [],[]

print("List 1: ")
for i in range(n):
	l1.append(int(input("Enter the element: ")))

print("List 2: ")
for i in range(n):
	l2.append(int(input("Enter the element: ")))
	
l1 = l1+l2
