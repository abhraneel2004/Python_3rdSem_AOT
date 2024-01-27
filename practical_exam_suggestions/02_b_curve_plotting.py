from matplotlib import pyplot as plt
from numpy import *

x = [i for i in range(5)]
y1 = [i for i in x]
y2 = [i*i for i in x]

plt.plot(x,y1, marker = "o", linewidth = "3", color = "blue", mfc = 'black', ms =1, label = "O(n)")
plt.plot(x,y2, marker = "o", linewidth = "3", color = "red", mfc = 'black', ms = 1, label = "O(n^2)")
plt.title("Time Complexity Plot")
plt.xlabel("x")
plt.ylabel("y")
plt.legend(loc = "lower right")
plt.grid()
plt.show()