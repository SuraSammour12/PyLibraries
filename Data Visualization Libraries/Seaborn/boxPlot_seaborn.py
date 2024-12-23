# Import libraries
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load the built-in 'tips' dataset from Seaborn
df=sns.load_dataset('tips')

# Set the figure size for the plot
plt.figure(figsize=(8,5))

# Create a box plot to show the distribution of total bill amounts by day and smoker status
# 'x' specifies the categorical variable (day of the week)
# 'y' specifies the numerical variable (total bill amount)
# 'hue' separates the data into categories based on smoker status (Yes/No)
sns.boxplot(data=df,x='day',y='total_bill',hue='smoker')

# Add a title to the plot
plt.title('Box Plot of Total Bill by Day and Smoker Status')

# Label the x-axis
plt.xlabel('Day')
# Label the y-axis
plt.ylabel('Total Bill')

# Save the plot as a PDF file named 'box_plot.pdf'
plt.savefig('box_plot.pdf', format='pdf')

# Display the plot
plt.show()