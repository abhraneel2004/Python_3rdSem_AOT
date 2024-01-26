x = int(input("Enter the number of items; "))

if x< 10:
	print('The total cost is: ', x*120)

elif x>=10 and x<=99:
	print('The total cost is: ', x*100)
	
elif x>=100:
	print('The total cost is: ', x*70)
