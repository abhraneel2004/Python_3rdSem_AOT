
def numinlist(l):
	c = 0
	for i in l:
		try:
			int(i)
			return True
		except:
			continue
	return False
	
l = eval(input("Enter the list: "))
print(numinlist(l))
