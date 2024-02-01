l = eval(input("Enter the list: "))
l1,l2 = [],[]
for i in l:
	if i not in l1:
		l1.append(i)
	else:
		l2.append(i)
l1.extend(l2)
print(l1)
