# Pandas Data Structures
#Pandas Series & Pandas DataFrames
# Create a Series from a Python list
import pandas as pd
# List
data=[10,20,30,40,50]
print("Type of data :",type(data))
data_series=pd.Series(data)
print("Type of data_series :",type(data_series))
print(data_series)
print('--------------------------------------------------------------')
lst=[5,10,15,20,25,30]
lst_series=pd.Series(lst,index=['a','b','c','d','e','f'])
print(lst_series)
print('--------------------------------------------------------------')
# Create a Series from a dictionary
dictionary_data={'a':10,'b':20,'c':30}
dic_series=pd.Series(dictionary_data)
print(dic_series)
print('--------------------------------------------------------------')
# Create a Series from a scalar value
scalar_series=pd.Series(100,index=['a','b','c','d','e'])
print(scalar_series)