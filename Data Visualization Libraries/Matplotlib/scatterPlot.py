import matplotlib.pyplot as plt
import numpy as np
"""
Importing Libraries:
matplotlib.pyplot is used for creating visualizations.
numpy is used for numerical operations.
"""
#This code creates a scatter plot to visualize the given data points, labels the axes, adds a legend, saves the output as a high-quality PDF file, and displays the plot

x = np.arange(1, 6)
y = np.array([3, 7, 2, 9, 5])
"""
Defining Data:
x: An array of values from 1 to 5 (used for X-axis coordinates).
y: An array of values corresponding to x (used for Y-axis coordinates).
"""
plt.figure(figsize=(10, 5)) # Initializes a figure with dimensions 10x5 inches
plt.scatter(x, y, color='red', label='Scatter Plot')
"""
Creating Scatter Plot:
Plots points at the coordinates defined by x and y.
The points are red (color='red') and labeled (label='Scatter Plot')
"""

# Adding Titles and Labels:

plt.title('Scatter Plot Example')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.legend() # Adds a legend to describe the plotted data.

plt.savefig('scatter_plot.pdf', format='pdf') # Saves the scatter plot as a high-quality PDF file named scatter_plot.pdf

plt.show() # Renders the scatter plot visually in the output