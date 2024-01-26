a = eval(input("Enter a list: "))
b = []
for k in a:
	if k not in b:
		b.append(k)
print(b)
