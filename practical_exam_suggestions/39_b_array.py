import numpy as np

l = np.random.randint(10,20,size=(3,3))
print("Original Matrix is: \n",l,"\n\n")
l = l.transpose()
l[1] = np.random.randint(10,20, size = 3)
l = l.transpose()
print("Updated Matrix is: \n",l)

'''

Algorithm:
step 1 - Create a Matrix using numpy
step 2 - Transpose the matrix 
step 3 - Change the 2nd row of the matrix
step 4 - Again transpose back the matrix (A')' = A

'''