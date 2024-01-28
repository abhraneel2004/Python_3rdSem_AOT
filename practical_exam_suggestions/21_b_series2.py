'''
The given series is:

2   5     8
- - -  +  -  - .... upto nth term
9   13    17

'''


def series2(n):
    sn = 0
    for i in range(1,n+1):
        an = (-1)**(i+1)
        t1 = (3*i)-1
        t2 = (4*i)+5
        an2 = t1/t2
        sn+= (an*an2)
    return sn


st = '''
The given series is:

2   5     8
- - -  +  -  - .... upto nth term
9   13    17

'''
print(st)
n = int(input("Enter the nth term: "))
print("Sumation of the series: ", series2(n))

# series2(n)