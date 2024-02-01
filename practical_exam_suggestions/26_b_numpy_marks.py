from matplotlib import pyplot as plt
import numpy as np

marks = np.random.randint(70, 100, size=5)
sub = ['Math', 'English', 'Chemistry','Hindi', 'Physics']

plt.plot(sub,marks, linewidth=2, marker="o", ms = 10, color="hotpink", mfc='blue' )
plt.title("Student Marks")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()