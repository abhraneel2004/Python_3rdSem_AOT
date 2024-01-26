n = int(input("Enter the no. of elements: "))
num, denum, frac = [],[], []

print("Enter numerator: ")
for i in range(n):
	x = int(input("Enter element: "))
	num.append(x)

print("Enter denomerator: ")
for i in range(n):
	x = int(input("Enter element: "))
	if x!=0:
		denum.append(x)
for i in range(n):
	frac.append(num[i]/denum[i])

print(max(frac))
print(min(frac))


