
n = eval(input("Enter the list of Employee ages (26-55): "))
c1,c2,c3 = 0,0,0
for i in n:
    if i>=26 and i<=35:
        c1+=1
    elif i>=36 and i<=45:
        c2+=1
    elif i>=46 and i<=55:
        c3+=1

print("Employees under 26-35: ", c1)
print("Employees under 36-45: ", c2)
print("Employees under 46-55: ", c3)