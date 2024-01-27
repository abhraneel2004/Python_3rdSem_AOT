
def fibo(n):
    if n==0 or n==1:
        return n
    return fibo(n-1)+fibo(n-2)

n = int(input("Enter the number of terms: "))
for i in range(0,n):
    print(fibo(i), end = " ")