# Merging and Joining Datasets
import pandas as pd

data1 = {
    'EmployeeID': [101, 102, 103, 104],
    'Name': ['Bella', 'Sura', 'Tasneem', 'Ghina'],
    'Department': ['HR', 'Finance', 'IT', 'Marketing']
}
data2 = {
    'EmployeeID': [101, 102, 103, 105],
    'Salary': [70000, 80000, 60000, 90000]
}

df1=pd.DataFrame(data1)
df2=pd.DataFrame(data2)

combined_sales=pd.concat([df1,df2])
# default axis=row // axis=0
print(combined_sales)

print('-----------------------------------------------------------------')

merged_df=pd.merge(df1,df2,on='EmployeeID')
print(merged_df)

print('--------------------------------------------------------')

inner_join_df=pd.merge(df1,df2,on='EmployeeID',how='inner')
print(inner_join_df)

print('--------------------------------------------------------')

outer_join_df=pd.merge(df1,df2,on='EmployeeID',how='outer')
print(outer_join_df)

print('--------------------------------------------------------')

left_join_df=pd.merge(df1,df2,on='EmployeeID',how='left')
print(left_join_df)

print('--------------------------------------------------------')

right_join_df=pd.merge(df1,df2,on='EmployeeID',how='right')
print(right_join_df)