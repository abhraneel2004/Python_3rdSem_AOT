p = int (input("enter Principle: "))
r = int (input("Enter rate: "))
t = int (input("Time: "))

print("Simple Interest is = ", (p*r*t)/100)

print("Compund Interest is = ", (p*((1+r/100)**t)-1))

