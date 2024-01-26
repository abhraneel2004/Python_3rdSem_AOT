n = int(input("enter n: "))
l = []
for i in range(n):
	x = int(input("Enter a number: "))
	l.append(x)

l.sort()
l = set(l)
l = list(l)
print(l[-2])
