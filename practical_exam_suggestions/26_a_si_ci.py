p = int (input("enter Principle: "))
r = int (input("Enter rate: "))
t = int (input("Time: "))

si = (p*r*t)/100
print("Simple Interest is = ", si)
print("Amount Payable is = ", p+si)


ci = p*((1+r/100)**t)
print("Compund Interest is = ", ci-p )
print("Amount Payable is = ", ci)


