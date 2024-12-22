import pandas as pd
employees=pd.DataFrame({
    'EmployeeID': [1, 2, 3, 4],
    'Name': ['Sura', 'Karim', 'Omar', 'Hiba'],
    'DeptID': [101, 102, 101, 103],
    'Additional1':['add1','add2','add3','add4'],
    'Additional2':['add1','add2','add3','add4'],
    'Additional3':['add1','add2','add3','add4']

})
print(employees)
print("----------------------------------------------------")
# Drop one column
employees=employees.drop(columns='Additional1')
print(employees)
print("----------------------------------------------------")
# Drop multiple columns
# method-1
# employees=employees.drop(columns=['Additional2','Additional3'])
# or method-2
employees.drop(columns=['Additional2','Additional3'],inplace=True)
print(employees)
print("----------------------------------------------------")
# rows to append to data frame one
rows=pd.DataFrame({'EmployeeID':[5,6],'Name':['Ali','Yafa'],'DeptID':[105,106]})
print(rows)
print("----------------------------------------------------")
# Appending new rows using (concat) to employees df
new_employees=pd.concat([employees,rows],axis=0)
"""
employees,rows:both are DataFrames
axis=0:this mean working on rows 
axis=1:this mean working on columns
"""
print(new_employees) 
print("----------------------------------------------------")
"""
we need to reset index because indices now 
for Ali and Yafa is append as it is :0,1 
so using reset_index() will fix this issue 
"""
# new_employees=new_employees.reset_index()
# print(new_employees)
# OR 
new_employees.reset_index(drop=True,inplace=True)
print(new_employees)
print("----------------------------------------------------")
""" dropping rows """
# method-1
new_employees.drop(index=[3,5],inplace=True) # this one is better 
# Or
# employees=employees.drop(index=[3,5])
print(new_employees)
print("----------------------------------------------------")
# dropping using condition
rows_to_drop=new_employees[new_employees['Name']=='Ali'].index # note :using .index
print(rows_to_drop) # index:4
new_employees.drop(index=rows_to_drop,inplace=True)
print(new_employees)