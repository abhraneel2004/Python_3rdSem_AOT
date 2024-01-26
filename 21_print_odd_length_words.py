s = input("Enter a string: ")

l = s.split(" ")

for i in l:
	if not len(i)%2:
		print(i)
