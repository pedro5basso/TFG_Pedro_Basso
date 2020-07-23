import matplotlib.pyplot as plt

list_clust = [1,1,2,2,3,4,4,4,4,4,5,5,6,7,8,8,8,9]
last_clust = list_clust[-1]

list_n_times = []

for i in range(0,last_clust):
    n_times = list_clust.count(i+1)
    list_n_times.append(n_times)

# Data to plot
labels = ['a', 'b','c','d','e','f','g','h','i']
sizes = list_n_times
colors = ['silver','rosybrown', 'lightcoral','navy', 'maroon', 'red', 'tomato','sienna','peru']
# explode = (0, 0)  # explode 1st slice

# Plot
plt.pie(sizes,  labels=labels, colors=colors,
autopct='%1.1f%%', shadow=False, startangle=140)

plt.axis('equal')
plt.show()