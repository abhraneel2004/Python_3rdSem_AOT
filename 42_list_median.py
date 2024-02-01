#median

def median(*args):
	l = list(args[0])
	l.sort()
	n = len(l)
	if (not n%2):
		return [l[(n-1)//2],l[n//2]]
	return l[(n-1)//2]	
	
a = eval(input("Enter your list: "))
print(median(a))
