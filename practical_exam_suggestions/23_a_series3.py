
def factorial(n):
    if n==0 or n==1:
        return 1
    return n*factorial(n-1)

def series3(n):
    sum_ = 0
    for i in range(1, n+1):
        ai = 1/factorial(i)
        sum_+=ai
    return sum_

st = '''

The given series is:

1    1    1
-  + -  + - + .... upto nth term
1!   2!   3!
'''
print(st)

t = int(input("Enter the number of terms: "))
print("Sumation of the series is: ", series3(t))