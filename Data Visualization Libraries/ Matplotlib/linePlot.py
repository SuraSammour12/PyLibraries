import matplotlib.pyplot as plt
import numpy as np
"""
Importing Libraries:
matplotlib.pyplot is used for creating visualizations.
numpy is used for numerical operation
"""
# This sequence creates and displays a line plot with labeled axes and a legend, and it saves the plot as an image

x=np.arange(1,6)
y=np.array([3,7,2,9,5])
"""
Defining Data:
x: An array of values from 1 to 5 (used for the X-axis).
y: An array of Y-axis values corresponding to x.
"""


fig=plt.figure(figsize=(10,5)) # Initializes a figure with dimensions 10x5 inches
plt.plot(x,y,marker='o',color='b',label='Line Plot')
"""
Plotting the Line:
x and y values are plotted as a line with circular markers ('o'), blue color ('b'), and a label ('Line Plot').
"""

# Adding Titles and Labels:

plt.title('Line Plot Example')
plt.xlabel('x-axis')
plt.ylabel('y-axis')

plt.legend() # Adds a legend to the plot to show the label defined earlier

plt.savefig('line_plot.png',format='png') # Saves the plot as a PNG image with the name line_plot.png

plt.show() # Renders the plot visually in the output