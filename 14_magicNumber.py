a = int(input("Enter a number: "))
c = 0
s = str(a)
while (len(s)>1 and c<1000):
	a = str(a)
	l = [int(x) for x in a]
	s = sum(l)
	a = s
	s = str(s)
	c+=1

if c>999:
	print("Not a magic number")
	
else:
	print("Magic number")
