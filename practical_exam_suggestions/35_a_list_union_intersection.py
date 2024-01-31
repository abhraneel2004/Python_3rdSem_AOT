

def uni(l1, l2):
    l3 = []
    for i in l1:
        if i not in l3:
            l3.append(i)
    for i in l2:
        if i not in l3:
            l3.append(i)
    return l3

def inter(l1, l2):
    l3 = []
    for i in l1:
        if (i in l2) and (i not in l3):
            l3.append(i)
    return l3

l1 = eval(input("Enter list 1: "))
l2 = eval(input("Enter list 2: "))
print("Union of two list: ",uni(l1, l2))
print("Intersection of two list: ",inter(l1, l2))