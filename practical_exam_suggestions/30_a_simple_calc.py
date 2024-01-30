c = 1
while c!=0:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("1. Add +")
    print("2. Subtract - ")
    print("3. Multiply * ")
    print("4. Divide / ")
    k = int(input("Enter your choice: "))
    if k==1:
        print(f"{a}+{b} = {a+b}")
    elif k==2:
        print(f"{a}-{b} = {a-b}")
    elif k==3:
        print(f"{a}*{b} = {a*b}")
    elif k==4:
        print(f"{a}/{b} = {a/b}")
    else:
        print("invalid choice")
        continue
    k2 = input("Exit? (y/n): ")
    if k2=='y':
        c=0