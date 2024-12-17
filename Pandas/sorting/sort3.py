import pandas as pd
data = {
    'Name': ['Yafa', 'Karam', 'Emad', 'Zain',"Emad","Karam"],
    'Age': [25, 30, 25, 22, 30,22],
    'Grade': [88, 75, 92, 85, 90,86]
}
df=pd.DataFrame(data)
print(df)
print('-------------------------------------------------------')
# Sort by age in ascending order and grade in descending order
df_sorted=df.sort_values(by=['Age','Grade'],ascending=[True,False])
print(df_sorted)
print('-------------------------------------------------------')
df_sorted.reset_index(drop=True,inplace=True)
print(df_sorted)