

def bubbleSort(l):
    n = len(l)
    for i in range(n):
        c = 0
        for j in range(0,n-i-1):
            if (l[j]>l[j+1]):
                l[j], l[j+1] = l[j+1], l[j]
                c = 1
        if not c:
            break
    return l

l = eval(input("Enter the list: "))
print(bubbleSort(l))
