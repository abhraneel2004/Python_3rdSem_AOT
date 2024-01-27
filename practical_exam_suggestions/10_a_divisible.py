
def divisible(n,m):
    for i in range(1, n+1):
        if i%m==0:
            if i%2==0:
                print(i,"EVEN")
            else:
                print(i, "ODD")

n = int(input("Enter a number: "))
m = int(input("Enter the second number:  "))
divisible(n,m)
