import matplotlib.pyplot as plt

# genetic_data = 'cgtacgttgacgtgcgtacgtgcgaggggtatacgta'
# base_counts = [genetic_data.count(val) for val in 'acgt']
# plt.bar(['A', 'C', 'G', 'T'], base_counts)
# plt.show()

#Here we define our data
times = [0, 1, 2, 3, 4, 5]
speeds = [0, 1.5, 2, 2.5, 3, 3.5]
#Create the plot
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
#Display the plot
ax.set_ylabel('Speeds (m/s)')
ax.set_xlabel('Time (s)')
ax.set_title('Robot Speed')
plt.show()

fig = plt.figure()  # Creates the figure that the subplots are add onto.
ax1 = fig.add_subplot(2, 2, 1)  # Imagine all the plots you want to add in a grid, (2,2) gives a 2x2 figure of grid.
ax1.set_title("Axis 1")
ax2 = fig.add_subplot(2, 2, 2)  # The last argument is the numeric label of the plot, as there is 4 plots, it ranges from 1 to 4. 
ax2.set_title("Axis 2")
ax3 = fig.add_subplot(2, 2, 3)
ax3.set_title("Axis 3")
ax3 = fig.add_subplot(2, 2, 4)
ax3.set_title("Axis 4")
plt.show()