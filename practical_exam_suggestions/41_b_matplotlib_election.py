import matplotlib.pyplot as plt

# Step 2: Prepare the data
sizes = []
labels = ['X','Y','Z']
for i in labels:
    seat = int(input(f"Enter the number of seats Party {i} got: "))
    sizes.append(seat)
idx = sizes.index(max(sizes))
explode = [0,0,0]  # Explode the second slice (B)
explode[idx] = 0.1
explode = tuple(explode)

# Step 3: Create the pie chart
plt.figure(figsize=(6, 6))
plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', startangle=140)

# Step 4: Add title and labels
plt.title('Pie Chart Example')

# Step 5: Show the pie chart
plt.show()
