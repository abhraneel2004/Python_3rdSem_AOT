

def checkbinary(s):
	for i in s:
		if not (i=='0' or i=='1'):
			return False
	return True
	
	
s = input("Enter a string: ")
if checkbinary(s):
	print("Yes")
else:
	print("No")
