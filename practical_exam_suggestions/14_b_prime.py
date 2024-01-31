def primenum(n):
    if n==0 or n==1 or (n>2 and n%2==0):
        return False
    if n==2:
        return True
    for i in range(3,int(n**0.5)+1,2):
        if (n%i==0):
            return False
    return True

n = int(input("Enter a number: "))
if (primenum(n)):
    print(f"{n} is a Prime number")
else:
    print(f"{n} is not a Prime number")