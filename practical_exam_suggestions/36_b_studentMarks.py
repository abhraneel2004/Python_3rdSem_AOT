import numpy as np

marks = np.random.randint(70,100,size=(5,6))
print("Original Marks:\n",marks)

#Increment 5
for i in range(len(marks)):
    for j in range(len(marks[i])):
        marks[i][j]+=5

print("Final Marks:")
for i in range(len(marks)):
    print(f"Marks of Student {i+1}: ")
    for j in range(len(marks[i])):
        print(f"Subject {j+1}: {marks[i][j]}")

