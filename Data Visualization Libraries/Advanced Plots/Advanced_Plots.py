# Import libraries
import seaborn as sns 
import matplotlib.pyplot as plt
import pandas as pd

# Load the built-in 'iris' dataset from Seaborn
df=sns.load_dataset('iris')

# Create a pair plot to visualize relationships between features
# 'hue' colors the points based on the species of the flower
# 'palette' sets the color scheme to 'Dark2' for better distinction
# 'markers' assigns different shapes to points for each species
sns.pairplot(df,hue='species',palette='Dark2',markers=['o','s','D'])

# Add a title to the pair plot and adjust its position
plt.suptitle('Pair Plot of Iris Features by Species',y=1.02)

# Save the pair plot as a PDF file named 'adv1.pdf'
plt.savefig('adv1.pdf', format='pdf')

# Display the pair plot
plt.show()
