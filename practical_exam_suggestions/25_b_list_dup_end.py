

l = eval(input("Enter the list:     "))
l2 = []
l3 = []
for i in l:
    if i not in l2:
        l2.append(i)
    else:
        l3.append(i)
l2 = l2 + l3
print("New List is: ", l2)