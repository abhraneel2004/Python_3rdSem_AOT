from matplotlib import pyplot as plt
from numpy import *

y1 = [87,88,90,94,95]
y2 = [76, 89,85,81,90]
x2 = ['english', 'chemistry', 'physics', 'math', 'cs']

plt.plot(x2,y1, linestyle= 'dotted', marker = "o", linewidth = "3", color = "blue", mfc = 'black', ms = 10, label = "Student 1 Marks")
plt.plot(x2,y2, linestyle= 'dotted', marker = "o", linewidth = "3", color = "red", mfc = 'black', ms = 10, label = "Student 2 Marks")
plt.title("Student Grade Graph")
plt.xlabel("Subject Name")
plt.ylabel("Marks")
plt.legend(loc = "lower right")
plt.grid()
plt.show()