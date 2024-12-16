import pandas as pd
import numpy as np
# Merging data frames
# Example
# df1
data1={
    'ID':[1,2,3,4],
    'Name':['Dania','Nezar','Saleem','Ahmad']
}
# df2
data2={
    'ID':[3,4,5,6],
    'Age':[23,24,25,26]
}
df1=pd.DataFrame(data1)
df2=pd.DataFrame(data2)
print(df1)
print("--------------------------------------------------------")
print(df2)
print("--------------------------------------------------------")
# INNER JOIN ,Intersection
# inner join (Default) An inner join returns only the rows where the keys match in both DataFrames.
"""
inner join 
df1=>1,2,3,4 | df2=>3,4,5,6
ID=>3,4<=
Result:ID(3,4)rows
(ID,Name,Age)
"""
inner_merged=pd.merge(df1,df2,on='ID',how='inner') 
print(inner_merged)
print("--------------------------------------------------------")
#left join returns all the rows from the left DataFrame (df1), and only matching rows from the right DataFrame (df2).
"""
df1(left)=>1,2,3,4 (ID,Name)
df2(right)=>3,4,5,6 (Age)
left join=>df1+(df2-age)column
"""
left_merged=pd.merge(df1,df2,on='ID',how='left')
print(left_merged)
print("--------------------------------------------------------")
#right join 
"""
df2(right)=>3,4,5,6
df1(left)=>1,2,3,4(Name)
right join=>df2+(df1-name)
"""
right_merged=pd.merge(df1,df2,on='ID',how='right')
print(right_merged)
print("--------------------------------------------------------")
#Outer Join : An outer join returns all the rows from both DataFrames, and NaN for missing matches
"""
df1+df2=>(ID : 1,2,3,4,5,6)
(ID,Name,Age)
"""
outer_merged=pd.merge(df1,df2,on='ID',how='outer')
print(outer_merged)