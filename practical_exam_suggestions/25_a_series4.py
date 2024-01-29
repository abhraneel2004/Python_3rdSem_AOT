
def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)

def series4(n,x):
    s = 0
    for i in range(1,n+1):
        t1 = (-1)**(i+1)
        t2 = x**i
        t3 = fact(i)
        ai = t1*t2/t3
        s+=ai
    return s

st = '''

The given series is:

x    x^2    x^3
-  -  -  +   -  - .... upto nth term
1!    2!     3!
'''
print(st)

n = int(input("Enter the number of terms (n): "))
x = int(input("Enter the value of x: "))
print("Sumation of the seris is: ", series4(n, x))
