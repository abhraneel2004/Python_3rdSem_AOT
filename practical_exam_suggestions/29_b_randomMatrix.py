import numpy as np
m1 = np.random.randint(1, 10+1, size=(3, 3))

m2 = np.random.randint(1, 10+1, size=(3,3))

print('\n-Matrix 1-\n',m1,'\n-------')

print('-Matrix 2-\n',m2,'\n-------\n')
sd = 0
for i in range(len(m1)):
    for j in range(len(m1[i])):
        if(i==j):
            sd+=(m1[i][j]+m2[i][j])
print("Sum of Diagonal Elements: ", sd)
