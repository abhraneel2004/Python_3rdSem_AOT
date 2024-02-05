#rainwater harvesting


'''

# Without Slicing

a = [0,1,0,2,1,0,1,3,2,1,2,1]
b= len(a)
water = 0

for i in range(1,b-1):
	left = a[i]
	for j in range(i):
		left = max(left,a[j])
		
	right = a[i]
	for j in range(i+1,b):
		right = max(right, a[j])
	water += min(left, right) - a[i]


print(water)

'''

# With Slicing

a = [0,1,0,2,1,0,1,3,2,1,2,1]
b= len(a)
water = 0
for i in range(1,b-1):
	left = max(a[i],max(a[:i]))
	
		
	right = max(a[i],max(a[i+1:b]))
	
	water += min(left, right) - a[i]
print(water)

