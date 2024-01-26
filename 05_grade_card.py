#grade problem

n = 5
x = 0
for i in range(n):
	x+=int(input("enter marks of subject:"))

x = x/n

if x >=91 and x<=100:
	print("O")
	
elif x >=81 and x<=90:
	print("A+")

elif x >=71 and x<=80:
	print("A")

elif x >=61 and x<=70:
	print("B")
	
elif x >=51 and x<=60:
	print("C")

elif x >=41 and x<=50:
	print("D")

elif x >=33 and x<=40:
	print("E")
	
else:
	print("F")


