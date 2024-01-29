
l = eval(input("Enter the list of strings: "))
if len(l)>0:
    idx = 0
    for i in l:
        if len(i)>len(l[idx]):
            idx = i
    print(len(l[idx]))
else:
    print("List must contain an element")