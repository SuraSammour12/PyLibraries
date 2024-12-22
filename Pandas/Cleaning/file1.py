import pandas as pd
import numpy as np
data = {
    'first': ['Mohammad', 'Abed', 'Omar', 'Emad', np.nan, None, 'NA'],
    'last': ['abu labun', 'battekh', 'shommam', 'khayyat', np.nan, np.nan, 'Missing'],
    'email': ['Mohammad@gmail.com', 'Abed@email.com', 'Omar@email.com', None, np.nan, 'Anonymous@email.com', 'NA'],
    'age': ['33', '55', '63', '36', None, None, 'Missing']
}
df=pd.DataFrame(data)
print(df)
print('-----------------------------------------------------------')
# Note:None And np.nan : missing values
# display missing values(True value --> means missing)
"""isnull(),isna()"""
# Method 1
missing=df.isnull()
print(missing)
print('-----------------------------------------------------------')
# Method 2
missingv=df.isna()
print(missingv)
print('-----------------------------------------------------------')
# Display the number of missing values in each column
print(df.isna().sum())
print('-----------------------------------------------------------')
# Display the number of missing values in the 'email' column
print(df['email'].isna().sum())
print('-----------------------------------------------------------')
"""Drop Missing Values(removes None,np.nan)"""
# dropna() 
print(df.dropna(axis=0,how='any')) #or axis='index')(rows)
# how="any": Drops the row (or column) if there is any missing value.
print('-----------------------------------------------------------')
print(df.dropna(axis=0,how='all'))
# how="all": Drops the row (or column) only if all values are missing.
print('-----------------------------------------------------------')
# columns 
print(df.dropna(axis=1,how='all')) # or axis='columns'
#print(df.dropna(axis=1,how='any')) # Drops columns that contain at least one missing value--> Empty DataFrame
print('-----------------------------------------------------------')
# dropping na based on a specific column
print(df.dropna(axis=0,subset='email'))
# in case multiple columne
print(df.dropna(axis=0,how='any',subset=['email','last']))
# (any) if the email | last => missing values ==> drop the rows
print(df.dropna(axis=0,how='all',subset=['email','last']))
# (all) if the email & last => missing valued ==> drop the row 









