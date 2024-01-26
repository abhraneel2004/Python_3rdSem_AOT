n = int(input("Enter a number: "))
for i in range(1,n+1):
	print(" "*(n-i), end = '')
	for i in range(0,i):
		print(i+1, end = ' ')
	print()

for i in range(n-1,0,-1):
	print(" "*(n-i), end = '')
	for i in range(0,i):
		print(i+1, end = ' ')
	print()
