import pandas as pd
df=pd.read_csv('metro.csv')
print(df)
# Handling Missing Values
df.fillna('-')# inplace=True
# NA,Missing != np.NaN,None
print(df)

df.dropna()# inplace=True
print(df)

df.dropna(axis=0)# default:rows
df.dropna(axis=1)# columns
print(df)

df.dropna(how='all')# inplace=True

# Keeps rows with at least 5 non-missing values, 
df.dropna(thresh=5)# inplace=True

print('----------------------------')

# Filling Missing Values : temp
mean_value=df['temp'].mean() # or median
df['temp'].fillna(mean_value,inplace=True)
print(df)

# Filling Missing Values : holiday
mode_value=df['holiday'].mode()[0] # Mode - The most common value
# why [0]?? # [0] is used to extract the first value from the most frequent values in the Series.
# Without [0], the code would attempt to replace missing values with the entire Series, which is not valid.

df['holiday'].fillna(mode_value,inplace=True)
print(df)

print('----------------------------')

""" backward , forward """
df=df.fillna(method='ffill') # forward : 37,np.nan,37==>37
#df=df.fillna(method='bfill') # backward : 36,np.nan,32==>36

print('----------------------------')

# df['holiday'].fillna('unknown',inplace=True)
df['holiday'].fillna('unknown',inplace=True)

# drops the 'temp' and 'rain_1h' columns from the DataFrame
df.drop(columns=['temp','rain_1h'],inplace=True)