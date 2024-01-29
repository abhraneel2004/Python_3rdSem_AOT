
def elesum(l1, l2,n):
    print("\n--------\nSum of matrix: ")
    for i in range(n):
        for j in range(n):
            print(l1[i][j]+l2[i][j], end = " ")
        print()

def elemul(l1, l2, n):
    print("\n--------\nElement multiplication of matrix: ")
    for i in range(n):
        for j in range(n):
            print(l1[i][j]*l2[i][j], end = " ")
        print()

def matmul(l1,l2,n):
    print("\n--------\nMatrix Multiplication of matrix: ")
    result = []
    for i in range(len(m1)):
        result.append([0] * len(m2[0]))
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(m2)):
                result[i][j] += m1[i][k] * m2[k][j]
    
    for i in range(len(result)):
        for j in range(len(result[i])):
            print(result[i][j], end = " ")
        print()
    

n = int(input("Enter the order of matrix: "))
m1 = []
m2 = []
print("Enter elements for Matrix 1: ")
for i in range(n):
    l = []
    for j in range(n):
        l.append(int(input(f"Enter element ({i},{j}): ")))
    m1.append(l)
print(m1)
print("Enter elements for Matrix 2: ")
for i in range(n):
    l = []
    for j in range(n):
        l.append(int(input(f"Enter element ({i},{j}): ")))
    m2.append(l)


print(m2)
elesum(m1,m2,n)
elemul(m1,m2,n)
matmul(m1,m2,n)