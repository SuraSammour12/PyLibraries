# Data Visualization with Seaborn
# Importing libraries
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load the built-in 'tips' dataset from Seaborn
df = sns.load_dataset('tips')

# Set the size of the plot
plt.figure(figsize=(8,5))

# Create a scatter plot with specific aesthetics
sns.scatterplot(data=df,x='total_bill',y='tip',hue='time',style='smoker')

# Add a title to the plot
plt.title('Scatter Plot of Total Bill Vs. Tip')

# Add labels to the axes
plt.xlabel('Total Bill')
plt.ylabel('Tip')

# Add a legend to the plot, specifying the legend title
plt.legend(title='Time of Day')

plt.savefig('scatter_plot_seaborn.pdf', format='pdf') # Saves the scatter plot as a high-quality PDF file named scatter_plot_seaborn.pdf

# Display the plot
plt.show()