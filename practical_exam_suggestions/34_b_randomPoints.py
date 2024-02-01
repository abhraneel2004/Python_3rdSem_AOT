from matplotlib import pyplot as plt
import numpy as np

n=30
x1 = np.random.randint(10,400, size = n)
y1 = np.random.randint(10,400, size = n)

plt.scatter(x1,y1, color ='red')
plt.title("Random Points")
plt.show()