# Pandas GroupBy and Aggregations
import pandas as pd
""" Aggregations Functions """
# mean() : Calculate the mean (average) value of the group or column
# std() : Calculate the standard deviation of the group or column
# median() : Calculate the median (middle) value of the group or column
# sum() : Calculate the sum of all the values of the group or column
# max() : Find the maximum value in the group or column
# min() : Find the minimum value in the group or column
# count() : Count the number of non-null (non-NaN) values in the group or column
# len() : Count the total number of rows, including NaN values

df=pd.read_csv('metro.csv')
# Group the data by the 'weather_main' column, resulting in groups based on unique values in this column
grouped=df.groupby('weather_main')
print(grouped.groups) # Print the total number of unique groups created by groupby.
print('***********************************************************')
# Print the total number of unique groups
print(f"Total number of unique groups: {len(grouped.groups)}")
print('***********************************************************')

# Print the unique group names
print(f"Unique weather types: {list(grouped.groups.keys())}")

print('----------------------------------------------------------------------')
# Apply multiple aggregation functions (len, sum, min, max, mean, median) to the 'temp' column for each group
print(grouped.temp.agg([len,sum,min,'max','mean','median'])) # built-in functions 

"""
functions can be written as text (e.g., 'max') or without quotes (e.g., max).
Difference:
Without quotes: Directly calls the Python function as an object.
With quotes: Refers to the string name of the function, supported by pandas.

"""
print('---------------------------------------------------------------------------')

print(df.dtypes) # Display the data type of each column in the DataFrame.

df['temp']=df['temp'].astype(int) # Convert the 'temp' column values to integers (from float).


print(grouped['temp'].agg('max').sort_values(ascending=False)) # Find the maximum 'temp' for each group and sort them in descending order.





