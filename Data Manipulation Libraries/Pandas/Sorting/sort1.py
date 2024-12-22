import pandas as pd
# Sorting DataFrame
data = {
    'Name': ['Yafa', 'Karam', 'Emad', 'Zain'],
    'Age': [22, 30, 35, 22],
    'Salary': [60000,50000, 70000, 55000]
}
df=pd.DataFrame(data)
print(df)
print('--------------------------------------------------------')
# sort by 'Age' ---> by default ascending order
df_sorted=df.sort_values(by='Age')
print(df_sorted)
print('--------------------------------------------------------')
"""
Sort by Age and then by Salary (if two people have the same age,
this sorts them by their salary)
"""
df_sorted2=df.sort_values(by=['Age','Salary'])
print(df_sorted2)
print('--------------------------------------------------------')
# sort by salary in descending order
df_sorted_descending=df.sort_values(by='Salary',ascending=False)
print(df_sorted_descending)
print('--------------------------------------------------------')
# Sort by Salary in descending order, and if salaries are equal, sort by Age in descending order.
df_sorted_descending2=df.sort_values(by=['Salary','Age'],ascending=False)
print(df_sorted_descending2)

