'''
1 
2 1 
4 2 1 
8 4 2 1 
16 8 4 2 1 

'''

n = int(input("Enter the number of rows: "))
for i in range(0,n+1):
    for j in range(i,-1,-1):
        print((2**j), end = " ")
    print()

'''
n = 5
i -> 0,1,2,3,4,5
j -> 1,0
range(1,5) 1,2,3,4
range(5,1) X
range(1,1) X
range(5,-1,-1) 5,4,3,2,1,0
'''

