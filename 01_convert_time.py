x = int (input("Enter the number of years: "))
temp = x
x = x*365
print('Days: ', x)
x = x*24
print("HOURS : ", x)
x = x*60
print("Minutes: ", x)
x *= 60
print('Seconds: ', x)

print(temp)

if temp%4==0:
	if temp%100==0 and temp%400!=0:
		print("Not a Leap Year")
	else:
		print("Leap Year")
else:
	print("Not a Leap Year")

