from matplotlib import pyplot as plt

parties = ['ABC', 'XYZ', 'MNP']
seats = [180, 200, 20]

plt.bar(parties, seats, color='blue', width=0.5)
plt.title("Election Results 2000", fontsize = 24)
plt.xlabel("Parties", fontsize=20, color='red')
plt.ylabel("Seat Count", fontsize=20)
plt.show()