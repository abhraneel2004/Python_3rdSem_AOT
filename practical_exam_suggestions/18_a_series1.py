'''
The given series is:

    1   1   1   1         1
1 + - + - + - + - + ... + -
    2   3   4   5         n

'''


def series1(n):
    s = 0
    for i in range(1, n+1):
        s+=(1/i)
    return s

n = int(input("Enter the number: "))
print(series1(n))