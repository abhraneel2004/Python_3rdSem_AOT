import numpy as np
import matplotlib.pyplot as plt

yax = []
for i in range(10):
    x = np.random.randint(6,10, size=40)
    y = sum(x)/len(x)
    y = round(y,2)
    yax.append(y)

xax = ['Section: '+str(i) for i in range(1,11)]

plt.plot(xax, yax, marker='o',ms=10, mfc = 'black', color='orange', linewidth=1.5)
plt.title("Average CGPA")
plt.xlabel("Sections")
plt.ylabel("Average CGPA")
plt.show()