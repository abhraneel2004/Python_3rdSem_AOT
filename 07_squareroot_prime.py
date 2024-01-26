

x = int(input("enter a number: "))

root = x**0.5
c = 0
for i in range(2, int(root**0.5)):
	if not root%i:
		c+=1
		break

if not c:
	print("Squareroot of", x, "is a prime number")

else:
	print("Squareroot of", x, "is not a prime number")
