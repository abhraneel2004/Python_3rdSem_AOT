def primenum(n):
    if n==2:
        return True
    if n==0 or n==1 or n%2==0:
        return False
    
    for i in range(3,int(n**0.5),2):
        if (n%i==0):
            return False
    return True
n = int(input("Enter a number(range): "))
l = []
for i in range(n+1):
    if (primenum(i)):
        l.append(i)
j = 0
l2 = []
while j<len(l):
    if j+1<len(l) and l[j+1]==l[j]+2:
        if l[j] not in l2:
            l2.append(l[j])
        if l[j+1] not in l2:
            l2.append(l[j+1])
    j+=1
for i in l2:
    print(i)
