# I am not supposed to know the code below 𓆝 𓆟 𓆞

 # Perform classification on the Iris dataset and visualize the feature correlations with a heatmap.

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.ensemble import RandomForestClassifier
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
iris = load_iris()
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

clf = RandomForestClassifier(random_state=42)
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

df = sns.load_dataset('iris')

numeric_df = df.select_dtypes(include=[np.number])
correlation_matrix = numeric_df.corr()

print(correlation_matrix)

sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', square=True, cbar_kws={'shrink': .8})
plt.title('Correlation Heatmap')

plt.savefig('correlation_heatmap.png', format='png')

plt.show()

print("---------------------------------------------------------------------")
# We start from here

# This code generates and visualizes the confusion matrix for the Iris dataset.
# First, it calculates the confusion matrix by comparing true labels (y_test) with predicted labels (y_pred).
# Then, it normalizes the confusion matrix to percentages for better understanding.
# The matrix is visualized as a heatmap using seaborn with labels representing the class names.
# The result is saved as a PNG image and displayed.

cm = confusion_matrix(y_test, y_pred)

# The first option prints the confusion matrix with actual counts of predictions,
# while the second option normalizes it to percentages for easier comparison.
print(cm)
#cm = cm / cm.sum() * 100
#print(cm)

plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='.2f', cmap='Blues', xticklabels=iris.target_names, yticklabels=iris.target_names)
plt.xlabel('Predicted Labels')
plt.ylabel('True Labels')
plt.title('Confusion Matrix for Iris Dataset')
plt.savefig('Confusion_Matrix.png', format='png')
plt.show()