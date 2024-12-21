# Pandas GroupBy and Aggregations
import pandas as pd

# Create a DataFrame with three columns: A, B, and C.
df = pd.DataFrame({'A' : ['foo', 'bar', 'foo', 'bar','foo', 'bar'],
                   'B' : [1, 2, 3, 4, 5, 6],
                   'C' : [2.0, 5., 8., 1., 2., 9.]})

# Group the DataFrame by column 'A'.
grouped=df.groupby('A')
print(grouped.groups)
"""{'bar': [1, 3, 5], 'foo': [0, 2, 4]}"""

# Filter groups where the mean of column 'B' is greater than 3.
df2=grouped.filter(lambda x:x['B'].mean() > 3)
# Mean of 'B' for 'foo': (1+3+5)/3 = 3 (not included).
# Mean of 'B' for 'bar': (2+4+6)/3 = 4 (included).
print(df2)

# Filter groups where the sum of column 'C' equals 15.
print(grouped.filter(lambda x:x['C'].sum()==15))
# Sum of 'C' for 'foo': 2+8+2 = 12 (not included).
# Sum of 'C' for 'bar': 5+1+9 = 15 (included).

# Apply the describe() function to each group and print the results.
print(grouped.apply(lambda x:x.describe()))
# Shows statistics like mean, std, min, max for each group.

print('----------------------------------------------')

# Define a function that calculates the demeaned values for a group.
def f(group):
    return pd.DataFrame({'original': group,'demeaned': group-group.mean()})
                # Original values of the group.       # Subtract mean of the group from each value
# Apply the function 'f' to column 'C' of each group
print(grouped['C'].apply(f)) 

# For each group in column 'C', create a DataFrame with original and demeaned values.






  
   