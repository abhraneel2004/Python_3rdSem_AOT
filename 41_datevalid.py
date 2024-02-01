

def leapyear(temp):
	if temp%4==0:
		if temp%100==0 and temp%400!=0:
			return 28
		else:
			return 29
	else:
		return 28


d = [31,28,31,30,31,30,31,31,30,31,30,31]

date = int(input("Enter Date (dd): "))
month = int(input("Enter Month (mm): "))
year = int(input("Enter Year (yyyy): "))

if date>0 and date<=31 and month>0 and month<13 and year <=2023:

	if month==2 and date<=leapyear(year) and date<=29:
		print("Valid Date")
	elif date<=d[month-1]:
		print("Valid Date")
	else:
		print("Invalid Date")

else:
	print("Invalid Date")
	
	
