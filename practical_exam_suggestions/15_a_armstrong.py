
def armstrong(n):
    l = len(str(n))
    sum=0
    temp =n
    while(temp>0):
        r = temp%10
        sum+=(r**l)
        temp = temp//10
    return sum==n

n = int(input("Enter a number: "))
if armstrong(n):
    print(f"{n} is an armstrong number")
else:
    print(f"{n} is not an armstrong number")