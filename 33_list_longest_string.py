
def longstr(l):
	d = {1:[0,len(l[0])]}
	for i in range(len(l)):
		x = len(l[i])
		if x>d[1][1]:
			d[1] = [i, x]
			
	print(l[d[1][0]])
	
l = eval(input("Enter the list: "))
longstr(l)
