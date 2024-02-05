
def primenum(n):
    if n==0 or n==1 or (n>2 and n%2==0):
        return False
    if n==2:
        return True
    for i in range(3,int(n**0.5)+1,2):
        if (n%i==0):
            return False
    return True


def factors(n):
    return [i for i in range(1,n+1) if n%i==0]

def uglyNum(n):
    if n==1:
        return True
    l = factors(n)
    l2 = [i for i in l if primenum(i)==True]
    for i in l2:
        if i not in (2,3,5):
            return False
    return True

a = int(input("Enter a number: "))
if(uglyNum(a)):
    print("The Number is Ugly")
else:
    print("The Number is NOT Ugly")

'''
Algorithm:
1. Find the factors of given number.
2. Check if the factors are prime
3. Check if the list of factors contain any prime number other than 2,3 or 5
4. Return False if the condition satisfies
5. Otherwise, return False
'''