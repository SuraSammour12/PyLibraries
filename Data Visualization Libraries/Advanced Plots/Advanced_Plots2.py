# Import libraries
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd 

# Load the built-in 'iris' dataset from Seaborn
df=sns.load_dataset('iris')

# Set the figure size for the plot
plt.figure(figsize=(8,6))


# Plot histograms with KDE for petal length distribution by species
# Iterate through each species and plot its petal length distribution
for species in df['species'].unique():
    sns.histplot(df[df['species']==species]['petal_length'],kde=True,label=species,bins=15)

# Add a title to the plot
plt.title('Petal Length Distribution by Species')
# Label the x-axis 
plt.xlabel('Petal Length (cm)')
# Label the y-axis 
plt.ylabel('Frequency')

# Add a legend to distinguish between species
plt.legend(title='Species')

# Save the plot as a PDF file named 'adv1.pdf'
plt.savefig('adv2.pdf', format='pdf')

# Display the plot
plt.show()