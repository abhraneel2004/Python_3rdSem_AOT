import numpy as np
print("For Matrix 1")

ar1 = np.array([[1,2,3],[4,5,6],[7,8,9]])



# print("Row wise minimum")

# for i in range(3):
#     print(np.amin(ar1[i],0))

# for i in range(3):
#     print(np.amax(ar1[i],0))

print("Row wise minimum:")
print(np.amin(ar1, axis=1))

print("Row wise maximum:")
print(np.amax(ar1, axis=1))

print("Column wise minimum:")
print(np.amin(ar1, axis=0))

print("Column wise maximum:")
print(np.amax(ar1, axis=0))

