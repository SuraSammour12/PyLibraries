# Import libraries
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load the built-in 'tips' dataset from Seaborn
df=sns.load_dataset('tips')

# Set the figure size for the plot
plt.figure(figsize=(8,5))

# Create a bar plot to show the average total bill for each day, separated by gender
# 'x' specifies the day of the week (categorical variable)
# 'y' specifies the total bill amount
# 'hue' separates the bars by gender (male and female)
# 'ci="sd"' adds error bars to represent the standard deviation
sns.barplot(data=df,x='day',y='total_bill',hue='sex',ci='sd')

"""
ci ==> confidence interval
sd ==> Standard Deviation
Add error bars representing the standard deviation (sd) of the data for each group
This shows the spread or variability of the total bill values around the mean
"""
# Add a title to the plot
plt.title('AverageTotal Bill Per Day')

# Label the x-axis
plt.xlabel('Day')
# Label the y-axis
plt.ylabel('Total Bill')

# Save the plot as a high-quality PDF file named bar_plot_seaborn.pdf
plt.savefig('bar_plot_seaborn.pdf', format='pdf') # Saves the bar plot as a high-quality PDF file named bar_plot_seaborn.pdf

# Display the plot on the screen
plt.show()
