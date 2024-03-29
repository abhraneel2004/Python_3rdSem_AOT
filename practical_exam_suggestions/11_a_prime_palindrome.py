
def palindrome(n):
    return str(n)==str(n)[::-1]

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

for i in range(n+1):
    if(primenum(i) and palindrome(i)):
        print(i, end = "\t")
