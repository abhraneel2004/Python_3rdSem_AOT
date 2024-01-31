n = int(input("Enter N: "))
l = []
for i in range(n):
    l.append(int(input(f"Enter {i+1} number: ")))

print("Maximum: ", max(l))
l.remove(max(l))
print("Second Maximum: ", max(l))