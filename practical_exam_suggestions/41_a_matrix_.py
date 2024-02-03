import numpy as np


n = int(input("Enter the order of matrix: "))
mat = np.random.randint(10,100,size = (n,n))
print("Original Matrix: \n",mat,'\n\n')

arr = list(mat[1])
arr.sort()
mat[1] = np.array(arr)
print("2nd Row Sorted: \n",mat, '\n\n')