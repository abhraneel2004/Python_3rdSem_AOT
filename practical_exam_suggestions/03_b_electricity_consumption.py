from matplotlib import pyplot as plt
import numpy as np

bills = np.random.randint(500,1300,12)
month = np.array(['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC'])

plt.plot(month, bills, marker='o', ms = 5)

plt.title("Monthly Electricity Bills", loc = "left")
plt.xlabel("Month")
plt.ylabel("Bills (in Rupees)")

plt.show()