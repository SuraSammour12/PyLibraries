# Merging data frames
import pandas as pd
# creating a DataFrame for employees
employees = pd.DataFrame({
    'EmployeeID': [1, 2, 3, 4],
    'Name': ['Sura', 'Alexei', 'Dmitry', 'Sara'],
    'DeptID': [101, 102, 101, 103]
})

# creating another DataFrame for departments
departments = pd.DataFrame({
    'DeptID': [101, 102, 103],
    'DeptName': ['HR', 'IT', 'Finance']
})
print(employees)
print('---------------------------------------------------------')
print(departments)
print('---------------------------------------------------------')
merged_df1=employees.merge(departments,on='DeptID')
print(merged_df1)
print('---------------------------------------------------------')
merged_df2=departments.merge(employees,on='DeptID')
print(merged_df2)