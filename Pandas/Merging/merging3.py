# Merging data frames
import pandas as pd
# Merging on multiple keys
employee_df = pd.DataFrame({
    'EmployeeID': [1, 2, 3],
    'DepartmentID': [101, 102, 103],
    'EmployeeName': ['Sura', 'Karim', 'Omar']
})

# salary table
salary_df = pd.DataFrame({
    'EmployeeID': [1, 2, 3],
    'DepartmentID': [101, 102, 104],
    'Salary': [50000, 60000, 55000]
})
print(employee_df)
print('-------------------------------------------------')
print(salary_df)
print('-------------------------------------------------')
# merging on multiple keys: EmployeeID and DepartmentID
merged_df1=pd.merge(employee_df,salary_df,on=['EmployeeID','DepartmentID'],how='left')
print(merged_df1)
"""
Note
EmployeeID=>3 
df1=>employee_df(DepartmentID=103),df2=>employee_df(DepartmentID=104)
EmployeeID=>(left merge so it's =103)
and because the two columns['DepartmentID'&'EmployeeID' =>not match]
Salary=>NaN 
"""
print('-------------------------------------------------')
merged_df2=pd.merge(employee_df,salary_df,on=['EmployeeID','DepartmentID'],how='outer')
print(merged_df2)
"""
df1: EmployeeID   DepartmentID
         1             101
         2             102
         3             103 <=========
df2: EmployeeID   DepartmentID
         1             101            Unique rows, this mean both will be added in the merged_df2 
         2             102
         3             104 <=========   
"""
print('-------------------------------------------------')


