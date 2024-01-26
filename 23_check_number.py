
def checknum(s):
	for i in s:
		if ord(i)>=48 and ord(i)<=57:
			print(True)
			return
	print(False)
	return

s = input("Enter a string: ")
checknum(s)
