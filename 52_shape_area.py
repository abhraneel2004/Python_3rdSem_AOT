
def a_rec(l,b):
	print(l*b)

def a_cir(r):
	print(3.14*r*r)

def a_sq(s):
	print(s*s)

def a_tri(b,h):
	print(0.5*b*h)
	
print("hello world")
while True:
	print("1. Area of Circle: ")
	print("2. Area of Square: ")
	print("3. Area of Rectangle:")
	print("4. Area of Triangle: ")
	print("----------------------")
	c = int(input("Enter your choice (1-5): "))
	if c==3:
		l = int(input("Enter Length of the rectangle: "))
		b = int(input("Enter Breadth of the rectangle: "))
		a_rec(l,b)
	elif c==2:
		l = int(input("Enter side of the Square: "))
		a_sq(l)
	elif c==1:
		l = int(input("Enter Radius of the Circle: "))
		a_cir(l)

	elif c==4:
		h = int(input("Enter Height of the Triangle: "))
		b = int(input("Enter Base of the rectangle: "))
		a_rec(b,h)

	elif c==5:
		break
	else:
		print("Invalid Choice")
		continue
