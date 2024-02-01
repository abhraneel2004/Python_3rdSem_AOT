
def max_min(l):
	return (("Max",max(l), l.index(max(l))),("Min", min(l), l.index(min(l))))

a = eval(input("Enter the list: "))
print(max_min(a))
