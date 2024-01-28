
def cubNum(n):
    temp = n
    sum = 0
    while(temp>0):
        r = temp%10
        sum+=(r**3)
        temp//=10
    return sum==n

l1 = eval(input("Enter the list of numbers: "))
l2 = []
for i in l1:
    if cubNum(i):
        l2.append(i)

print("New List is: ",l2)
print("Maximum Element: ",max(l2))
print("Minimum Element: ",min(l2))