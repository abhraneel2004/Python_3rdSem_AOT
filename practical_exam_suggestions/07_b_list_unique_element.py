
def unique_(l):
    m = []
    for i in l:
        if i not in m:
            m.append(i)
    return m

l = eval(input("Enter the list: "))
print(unique_(l))