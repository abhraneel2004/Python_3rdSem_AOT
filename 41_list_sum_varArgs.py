def sumpos( *args):
	l = args
	sum=0
	for i in l[0]:
		if i>0:
			sum+=i
	return sum

a = eval(input("Enter arguments: "))
print(sumpos(a))
