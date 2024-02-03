

n = int(input("Enter the number: "))
k = int(input("Enter k: "))
l = [x for x in range(1,n+1) if n%x==0]
print(l)
m = len(l)-k
if m>=0 and m<len(l):
    print(f"{k}th Largest factor is {l[m]}")
else:
    print("List Index out of range")