
def checkallvow(s):
	l = 'aeiou'
	for i in s.lower():
		if i in l:
			l = l.replace(i,'')
	return not len(l)

s = input("Enter a string; ")
if checkallvow(s):
	print('Accepted')

else:
	print("Rejected")
