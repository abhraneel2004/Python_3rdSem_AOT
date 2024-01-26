
def removedup(s):
	l = []
	for i in s:
		if i not in l:
			l.append(i)
	return ''.join(l)
	
s = input("Enter a string: ")
print(removedup(s))
