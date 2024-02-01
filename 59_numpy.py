import numpy as np

ar = np.array([1,2,3])
print(ar)
print(ar.shape)
b = np.array([[1,2,3],[4,5,6]])
print(b.shape)
print(type(b))
print(b.size)

a2 = np.array([[1,2,3],[4,5,6]])
print(a2)
a2 = a2.reshape(3,2)
print(a2)

a3 = np.arange(24)
print(a3)

a3.ndim

b = a3.reshape(2,4,3)
print(b)