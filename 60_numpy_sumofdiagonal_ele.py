import numpy as np
ar = np.zeros((3,3), dtype = np.int8)
ar = ar.reshape(3,3)
for i in range(3):
    for j in range(3):
        ar[i,j] = int(input(f"Enter element ({i},{j}): "))
print("The given matrix is :\n",ar)
sum = 0
for i in range(3):
    sum+=ar[i,i]
print("sum of diagonal elements is: ", sum)