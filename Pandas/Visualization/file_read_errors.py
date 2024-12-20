# Troubleshooting Common File Reading Errors
import pandas as pd
""" Problem 1 """
"""
df_csv_1=pd.read_csv('metro_corrupted.csv')
print(df_csv_1)
"""
# pandas.errors.ParserError: Error tokenizing data. C error: Expected 9 fields in line 10, saw 10
# how to solve the problem
df_csv_1=pd.read_csv('metro_corrupted.csv',on_bad_lines='skip')#skip,warn,error
# default value (on_bad_lines => error)
print(df_csv_1)

print('-------------------------------------------------------------')
""" Problem 2 """
# df=pd.read_csv('metro.csv',dtype={'temp':'int'})
# ValueError: cannot safely convert passed user dtype of int64 for float64 dtyped data in column 1
# dtype={'temp':'int'} :Ensure the 'temp' column is of type int; raises an error if the data cannot be converted (e.g., contains non-numeric or float values)


# Read CSV file without specifying data types
df = pd.read_csv('metro.csv')

# Convert the 'temp' column to integer type after reading the data
df['temp'] = df['temp'].astype(int)

# Print the first few rows of the DataFrame to verify the data
print(df.head())

print('-------------------------------------------------------------')

""" Problem 3 """
# Handling Large Files in Chunks to Avoid Memory Overload
df_metro=pd.read_csv('metro.csv')
print(df_metro.count())

# Read file in chunks
df_metro=pd.read_csv('metro.csv',chunksize=10000)
print(df_metro)

counter=0
for chunk in df_metro:
    # print(chunk)
    counter+=1
print(counter)#48,000/10000=4.8~5