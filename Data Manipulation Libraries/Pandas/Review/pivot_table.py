# Pivot Table
import pandas as pd
"""
A pivot_table in pandas is a powerful tool for summarizing and reorganizing data in a DataFrame,
 allowing you to aggregate data based on specified keys. 
 It is commonly used to create summary tables that show aggregated values, 
 like sums, averages, or counts, across different categories.
 
"""
data = {
    'Category': ['Electronics', 'Electronics', 'Furniture', 'Furniture', 'Clothing', 'Clothing'],
    'Product': ['Laptop', 'Tablet', 'Chair', 'Table', 'Shirt', 'Pants'],
    'Month': ['January', 'January', 'February', 'February', 'January', 'February'],
    'Sales': [1500, 800, 450, 300, 200, 500]
}

df=pd.DataFrame(data)

pivot_table=df.pivot_table(values='Sales',index='Category',columns='Month',aggfunc='sum',fill_value=0)
"""
values='Sales': The column you want to aggregate.
index='Category': Rows will be grouped by this column.
columns='Month': Columns will represent different months.
aggfunc='sum': Aggregation function, summing up sales per category and month.
fill_value=0: Replaces missing values with 0.

"""
print(pivot_table)
