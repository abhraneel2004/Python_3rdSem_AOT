n = int(input("Enter The number of rows:    "))
for i in range(1,n+1):
    print(" "*(n-i), end = '')
    for j in range(1,i+1):
        print(j, end = " ")
    print()

for i in range(n-1,0,-1):
    print(" "*(n-i), end = '')
    for j in range(1,i+1):
        print(j, end = " ")
    print()