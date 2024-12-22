import pandas as pd
import numpy as np
# Dealing with none actual missing data ('Missing' ,'NA' (Texts))
data = {
    'first': ['Mohammad', 'Abed', 'Omar', 'Emad', np.nan, None, 'NA'],
    'last': ['abu labun', 'battekh', 'shommam', 'khayyat', np.nan, np.nan, 'Missing'],
    'email': ['Mohammad@gmail.com', 'Abed@email.com', 'Omar@email.com', None, np.nan, 'Anonymous@email.com', 'NA'],
    'age': ['33', '55', '63', '36', None, None, 'Missing']
}
df=pd.DataFrame(data)
print(df)
print('-------------------------------------------------------------')
# replacing not actual missing values with actual missing values
"""
df.replace('Missing',np.nan,inplace=True)
df.replace('NA',np.nan,inplace=True)

"""
#or
df=df.replace({'Missing':np.nan,'NA':np.nan})
print(df)
print('-------------------------------------------------------------')
print(df.isna().sum())
print('-------------------------------------------------------------')
# fillna values
print(df.fillna("missing"))# we can use any value we want (np.nan,none)
