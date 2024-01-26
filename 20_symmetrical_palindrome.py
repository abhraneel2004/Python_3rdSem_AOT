#symmertical or palindrome

def symmetrical(s):
	l = len(s)
	return s[:l//2] == s[l//2::]

def palindrome(s):
	return s==s[::-1]
	
string = input("Enter a string: ")
if symmetrical(string):
	print("The string is Symmetrical")
else:
	print("The String is NOT symmetrical")

if palindrome(string):
	print("The string is a Palindrome")
else:
	print("The string is not a Palindrome")

