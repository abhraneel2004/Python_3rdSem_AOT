import math

l = int(input("Enter the length of rectangle: "))
b = int(input("Enter the breadth of rectangle: "))
r = int(input("Enter the radius of circle: "))

print("Perimeter of rectangle: ", 2*(l+b))
print("Circumference of circle: ", math.pi*r*r)