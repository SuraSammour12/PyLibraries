# Pandas GroupBy and Aggregations
import pandas as pd
# read the csv file into DF
df=pd.read_csv('metro.csv')

# group the dataframe by 'weather_main column value
grouped=df.groupby('weather_main')

# print the groups with their indices
print(grouped.groups)

# get and print the rows where 'weather_main' is clouds
print(grouped.get_group('Clouds'))

# calculate the mean temperature for the 'Clouds' group
print(grouped.get_group('Clouds').temp.mean()) # this calculates the mean of the 'temp' column for 'Clouds'

# print the count of non-null values in each column for the 'Clouds' group
print(grouped.get_group('Clouds').count())

