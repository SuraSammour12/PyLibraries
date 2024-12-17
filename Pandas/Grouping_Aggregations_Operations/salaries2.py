import pandas as pd
df=pd.read_csv('ds_salaries.csv')
print(df)
# get unique values of a specific column
print(df['experience_level'].unique())

# convert it to a list. by using tolist()
print(df['experience_level'].unique().tolist())

# get number of unique items in specific column
print(df['experience_level'].nunique())

# imagine we don't have nunique function what would you do?
"""use set data structure because it Prevent duplicate"""

# Print the count of each unique value in the 'experience_level' column
print(df['experience_level'].value_counts())

# Print the count of each unique value in the 'job_title' column
print(df['job_title'].value_counts())

# Display the column names of the DataFrame
print(df.columns)

# convert it to a list. by using tolist()
print(df.columns.tolist())

# rename column
df.rename(columns={'work_year':'year'},inplace=True)
# dictionary {'work_year':'year'} => year : new column name

print(df)
    
