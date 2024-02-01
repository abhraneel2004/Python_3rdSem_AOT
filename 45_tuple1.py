a = (11, 22, 33, 44, 55, 66)
b = tuple()
for i in range(len(a)):
	if a[i]==44 or a[i]==55:
		b = b+(a[i],)
	
print(b)
