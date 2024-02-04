
def triangle(a,b,c):
    l = [a,b,c]
    l.sort()
    if l[2]<(l[0]+l[1]):
        if (a==b and a==c):
            print("Equilateral triangle")
            return
        elif (a==b or a==c or b==c):
            print("Isosceles Traingle")
            return
        print("scalane triangle")
        return
    print("Invalid triangle")
    return

a = int(input("Enter the side 1: "))
b = int(input("Enter the side 2: "))
c = int(input("Enter the side 3: "))

triangle(a,b,c)
