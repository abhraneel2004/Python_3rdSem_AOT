x = input("Enter a string: ")

arr = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
alphas = 'abcdefghijklmnopqrstuvwxyz'
for i in x:
	if i in alphas:
		arr[alphas.index(i)] +=1
flag = True		
for i in range(len(arr)):
	if not i:
		continue
	elif i+1==arr[i]:
		continue
	else:
		flag = False
		break
		
if flag:
	print("the given string is a Super ASCII string")
else:
	print("the given string is NOT a Super ASCII string")
