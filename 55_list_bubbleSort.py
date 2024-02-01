
def bubble_(l):
	n = len(l)
	swapped = False
	for i in range(n-1):
		for j in range(n-i-1):
			if l[j]>l[j+1]:
				temp = l[j]
				l[j] = l[j+1]
				l[j+1] = temp
				swapped = True
			if not swapped:
				break
	return l

a = eval(input("Enter the list: "))
print(bubble_(a))
