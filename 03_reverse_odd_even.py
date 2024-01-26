#reverse of a number

x = int(input("Enter a number: "))
print(int(str(x)[::-1]))

if x%2:
	print("Odd")
else:
	print("Even")
