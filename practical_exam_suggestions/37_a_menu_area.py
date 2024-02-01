from math import pi

c = 1
while c!=5:
    print("Area:")
    print("1. Circle")
    print("2. Square")
    print("3. Rectangle")
    print("4. Triangle")
    print("5. Exit")
    c = int(input("Enter your choice: "))
    if c==1:
        r = int(input("Enter the radius of the circle: "))
        print(f"Area of circle is : {pi*r*r}")
    elif c==2:
        s = int(input("Enter the side of square: "))
        print(f"Area of square is : {s*s}")
    elif c==3:
        l = int(input("Enter the length of rectangle:"))
        b = int(input("Enter the breadth of the rectangle: "))
        print(f"Area of rectangle is : {2*(l+b)}")
    elif c==4:
        b = int(input("Enter the base of triangle:"))
        h = int(input("Enter the height of the triangle: "))
        print(f"Area of triangle is : {0.5*b*h}")
    elif c==5:
        print("Exiting the program")
        break
    else:
        print("Invalid input. Refer to the Menu.")