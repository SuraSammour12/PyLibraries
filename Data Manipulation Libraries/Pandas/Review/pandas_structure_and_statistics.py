# Exploring Pandas Structure and Descriptive Statistics
import pandas as pd

# Load the Excel file and display the column names; unnamed columns will be automatically labeled as 'Unnamed: x'
df1=pd.read_excel('historical_temp.xlsx',)
print(df1.columns)# Un named columns

# Load the Excel file without treating the first row as column headers; columns will be numbered sequentially
df2=pd.read_excel('historical_temp.xlsx',header=None)
print(df2.columns)# Numbered columns

# Load the Excel file and assign custom names to the columns; excess columns will be ignored if names provided are fewer
df3=pd.read_excel('historical_temp.xlsx',names=['aaa','bbb'])
print(df3.columns)# Named columns

print('------------------------------------------------------------------')

df4=pd.read_csv('metro.csv') # Load the CSV file into a DataFrame
print(df4.describe()) # Display summary statistics for numeric columns
"""
Count: Number of non-missing values.
Mean: Average of the values.
Std: Standard deviation (measure of variability).
Min/Max: Minimum and maximum values.
25%, 50%, 75%: Percentile values (quartiles).
"""

print(df4.dtypes) # Prints the data types (dtypes) of each column in the DataFrame

print(df4.info()) # Provides a concise summary of the DataFrame

print(df4.columns) # This command outputs the names of all columns in the DataFrame

print(df4.index) # This command prints the index of the DataFrame

print(df4.shape) # This command returns a tuple representing the dimensions of the DataFrame: (number of rows, number of columns)


temp_mean=df4['temp'].mean()
temp_median=df4['temp'].median()
temp_std=df4['temp'].std()

print('Mean temperature:',temp_mean)
print('Median temperature:',temp_median)
print('Standard deviation of temperature:',temp_std)


print(df4.isnull().sum())
# isnull() : each element is a boolean value (True if the value is null or missing, False otherwise
# sum(): This sums the True values (which represent null values) for each column