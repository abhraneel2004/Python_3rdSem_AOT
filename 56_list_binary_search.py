

def binary_search(l, key):
	l.sort()
	print("Sorted list: ", l)
	low = 0
	u = len(l)-1
	m = (low+u)//2
	while (low<u):
		if key==l[m]:
			print("Fount at position : ",m)
			return
		elif key<l[m]:
			u = m
			m = (low+u)//2
		else:
			low = m
			m = (low+u)//2

a = eval(input("Enter the list: "))
key = int(input("Enter the value to search: "))
binary_search(a, key)
