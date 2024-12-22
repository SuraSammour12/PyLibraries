import pandas as pd
# Data Manipulation with Pandas

df=pd.read_csv('metro.csv')
print(df)

# Renames the 'temp' column to 'Temperature' in the DataFrame
df.rename(columns={'temp':'Temperature'},inplace=True)
print(df)

# Drops rows with indices 0 to 999 from the DataFrame
"""df=df.drop(index=[i for i in range(1000)])"""
# Then, prints the statistical summary of the updated DataFrame using describe()
print(df.describe())


# Strip any leading or trailing whitespace from the 'weather_main' column values.
df['weather_main']=df['weather_main'].apply(lambda x:x.strip())
# Convert the 'Temperature' column from Kelvin to Celsius by subtracting 273.15 from each value.
"""df['Temperature']=df['Temperature'].apply(lambda x:x-273.15)"""
print(df.describe())


one_column=df['traffic_volume'] # Series
two_columns=df[['Temperature','traffic_volume']] # DataFrame
print(one_column.count()) # count its non-null values
print(two_columns.count()) # count non-null values for each column individually


# Select the first two rows and specific columns by index (1, 2, 4) using iloc.
first_two_rows=df.iloc[0:2,[1,2,4]]
                       #rows  #columns
print(first_two_rows)
print('-----------------------------------------------------------------')
# Select rows from index 1 to 5 and two specific columns: 'holiday' and the second column by name using loc.
age_and_score=df.loc[1:5,['holiday',df.columns[1]]]
                     # note :row 5 is inclusive
print(age_and_score)


print('-----------------------------------------------------------------')

print(df['Temperature'].describe())
print('**************************************************************')
new_temps=df[df['Temperature']>300]
print(new_temps.describe())

print('-----------------------------------------------------------------')

filtered_df=df[(df['Temperature']>300)&(df['traffic_volume']>6000)] # | or
print(len(filtered_df)) # len(): number of rows in the filtered DataFrame.
print(filtered_df.describe())