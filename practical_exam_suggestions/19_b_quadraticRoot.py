
import math

def find_roots(a, b, c):
    # Calculate the discriminant
    discriminant = b**2 - 4*a*c

    if discriminant > 0:
        # Two real and distinct roots
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2
    elif discriminant == 0:
        # One real root (double root)
        root = -b / (2*a)
        return root,
    else:
        # Complex roots
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(abs(discriminant)) / (2*a)
        root1 = complex(real_part, imaginary_part)
        root2 = complex(real_part, -imaginary_part)
        return root1, root2


print("For equation: ax^2 + bx + c\n")
a = int(input("Enter the coefficient a: "))
b = int(input("Enter the coefficient b: "))
c = int(input("Enter the coefficient c: "))

roots = find_roots(a, b, c)

if len(roots) == 2:
    print(f"The roots of the quadratic equation are: {roots[0]} and {roots[1]}")
elif len(roots) == 1:
    print(f"The root of the quadratic equation is: {roots[0]}")
else:
    print(f"The roots of the quadratic equation are complex: {roots[0]} and {roots[1]}")