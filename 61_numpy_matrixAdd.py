import numpy as np
print("For Matrix 1")
ar1 = np.zeros((3,3), dtype = np.int8)
ar1 = ar1.reshape(3,3)
for i in range(3):
    for j in range(3):
        ar1[i,j] = int(input(f"Enter element ({i},{j}): "))
print("The given matrix is :\n",ar1)

print("For Matrix 2")
ar2 = np.zeros((3,3), dtype = np.int8)
ar2 = ar2.reshape(3,3)
for i in range(3):
    for j in range(3):
        ar2[i,j] = int(input(f"Enter element ({i},{j}): "))
print("The given matrix is :\n",ar2)

res = np.add(ar1,ar2)
print("The addition of Matrix 1 and Matrix 2 is: \n", res)