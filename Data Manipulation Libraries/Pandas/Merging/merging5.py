import pandas as pd
personal_info = pd.DataFrame({
    'EmployeeID': [101, 102, 103],
    'Name': ['Qusai', 'Raneem', 'Mona'],
    'Age': [25, 30, 35]
})

job_info = pd.DataFrame({
    'EmployeeID': [101, 102, 103],
    'Position': ['Developer', 'Designer', 'Manager'],
    'Salary': [70000, 60000, 80000]
})
print(personal_info)
print('-------------------------------------------------------------')
print(job_info)
print('-------------------------------------------------------------')
# Merge the two DataFrames
print(pd.merge(personal_info,job_info,on='EmployeeID',how='outer'))
print('-------------------------------------------------------------')
# merge the DataFrames side by side using axis=1 
combined_info=pd.concat([personal_info,job_info.drop(columns='EmployeeID')],axis=1)
print(combined_info)
print('-------------------------------------------------------------')

