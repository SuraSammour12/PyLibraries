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
print("-----------------------------------------------------")
df=df.replace({'Missing':np.nan,'NA':np.nan})
print(df)
print("-----------------------------------------------------")
# common way to filling missing values
df['age']=df['age'].astype(float) # casting

# Fill missing values with the mean of the age column
df['age']=df['age'].fillna(df['age'].mean())
print(df)