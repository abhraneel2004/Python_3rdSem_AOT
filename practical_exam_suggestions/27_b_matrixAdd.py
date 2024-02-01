import numpy as np

# Function to read a matrix from the user
def read_matrix():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    matrix = []
    print("Enter the elements row-wise:")
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(int(input(f"Enter element ({i},{j}): ")))
        matrix.append(row)
    return np.array(matrix)

# Read the first matrix
print("Enter details for Matrix 1:")
matrix1 = read_matrix()
if matrix1 is None:
    exit()

# Read the second matrix
print("Enter details for Matrix 2:")
matrix2 = read_matrix()
if matrix2 is None:
    exit()

# Check if the matrices have the same shape
if matrix1.shape != matrix2.shape:
    print("Error: Matrices should have the same shape for addition.")
    exit()

# Perform matrix addition
result_matrix = matrix1 + matrix2

# Save the result to a text file
filename = input("Enter the filename to save the result: ")
filename = filename+'.txt'
with open(filename, 'w') as file:
    file.write("Result of Matrix Addition:\n")
    for row in result_matrix:
        file.write(' '.join(map(str, row)) + '\n')

print("Result has been saved to", filename)
