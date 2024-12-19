# Loading Data from Different Sources and Inspecting It 
import pandas as pd

""" Read csv files """
df1=pd.read_csv('metro.csv',encoding='utf-8')
# default ==> sep=','
print(df1.columns)

print("--------------------------------------------------------------------------------")

""" Read excel files """
df2=pd.read_excel('historical_temp.xlsx')
print(df2.tail())

print("--------------------------------------------------------------------------------")

""" Read tsv files :Tab-separated values """
df3=pd.read_csv('sample-data.tsv',sep="\t")
print(df3.index)

print("--------------------------------------------------------------------------------")

""" Read json files :JavaScript Object Notation """
import json
df4=pd.read_json('iris.json')
# Print the axes of the DataFrame to display row indices and column names
print(df4.axes)

print("--------------------------------------------------------------------------------")

""" Read data from a SQL database using sqlite3 library"""
# Import the sqlite3 library to work with SQLite databases
import sqlite3 

# Connect to a SQLite database
conn = sqlite3.connect('database.sqlite')

# Read data from the 'Iris' table into a Pandas DataFrame
df = pd.read_sql("SELECT * FROM 'Iris'", conn)

# Print the 'SepalWidthCm' column for the first 4 rows (index 0 to 3)
print(df.loc[:3, 'SepalWidthCm'])

# Close the connection to the SQLite database
conn.close()
print("--------------------------------------------------------------------------------")

# this file extensions is used in data-heavy workflows.
df5=pd.read_parquet('iris.parquet')
print(df.iloc[:5])