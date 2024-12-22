import matplotlib.pyplot as plt
import numpy as np
"""
Importing Libraries:
matplotlib.pyplot is used for creating visualizations.
numpy is used for numerical operations.
"""
# This code creates a bar plot to visualize the given data, labels the axes, adds a legend, and saves the output as a JPG image file.

x=np.arange(1,6)
y=np.array([3,7,2,9,5])
"""
Defining Data:
x: An array of values from 1 to 5 (used for the X-axis, representing categories).
y: An array of values corresponding to x (used for the Y-axis, representing values).
"""
plt.figure(figsize=(10,5)) # Initializes a figure with dimensions 10x5 inches.
plt.bar(x,y,color='green',label='Bar Plot')
"""
Creating Bar Plot:
Plots vertical bars with X values as categories and Y values as their heights.
The bars are green (color='green') and labeled (label='Bar Plot').
"""
# Adding Titles and Labels:

plt.title('Bar Plot Example')
plt.xlabel('Categories')
plt.ylabel('Values')

plt.legend() # Adds a legend to describe the plotted data
plt.savefig('bar_plot.jpg',format='jpg') # Saves the bar plot as a JPG image file named bar_plot.jpg
plt.show() # Renders the bar plot visually in the output