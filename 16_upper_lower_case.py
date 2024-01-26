x  = input("Enter a string: ")
l = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
m = 'abcdefghijklmnopqrstuvwxyz'

lo,up = 0,0
for i in x:
	if i in l:
		up+=1
		continue
	elif i in m:
		lo+=1
		continue
		
print("UpperCase letters in string: ",up)
print("LowerCase letters in string: ",lo)

