x = input("Enter a string: ").lower()
arr = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
alphas = 'abcdefghijklmnopqrstuvwxyz'
for  i in x:
	if i in alphas:
		arr[alphas.index(i)] = 1
		
if 0 in arr:
	print("Not a Panagram")
else:
	print("Panagram")
