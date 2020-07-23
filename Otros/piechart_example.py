import matplotlib.pyplot as plt

# Data to plot
labels = 'Similarity', 'No Similarity'
sizes = [269, 28]
colors = ['green', 'red']
explode = (0, 0)  # explode 1st slice

# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=False, startangle=140)

plt.axis('equal')
plt.show()