
n = int(input("Enter the number of elements of a list: "))
l1 = []
l2 = []
l3 = []
print("Enter the element for List1: ")
for i in range(n):
    l1.append(int(input(f"Enter element l1[{i}]: ")))

print("Enter the element for List2: ")
for i in range(n):
    l2.append(int(input(f"Enter element l2[{i}]: ")))

for i in range(n):
    l3.append(l1[i]+l2[i])

print("Result of their sumation: ", l3)