
def perfect(n):
    sum=0
    for i in range(1, (n//2)+1):
        if n%i==0:
            sum+=i
    return sum==n

n = int(input("Enter a number: "))
if (perfect(n)):
    print(f"The given number {n} is perfect")
else:
    print(f"The given number {n} is NOT perfect")