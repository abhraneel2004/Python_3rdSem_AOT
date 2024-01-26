a = int(input("Enter a number: "))
if (a == int(str(a)[::-1])):
	print(a, "is a palindrome")
else:
	print(a, "is not a palindrome")
