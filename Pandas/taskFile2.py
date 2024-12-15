#2_Pandas_Updating_Removing_Adding_rows_and_columns-Last Task
import pandas as pd
import numpy as np
data = [
    {'Product': 'Laptop', 'Price': 1200, 'Quantity': 5, 'Discount': 10},
    {'Product': 'Tablet', 'Price': 600, 'Quantity': 10, 'Discount': 15},
    {'Product': 'Smartphone', 'Price': 800, 'Quantity': 7, 'Discount': 5},
    {'Product': 'Monitor', 'Price': 300, 'Quantity': 12, 'Discount': 20}
]
df=pd.DataFrame(data)
print(df)
print('---------------------------------------------------------------------')
df['High_Price']=np.where(df['Price']>700,'yes','no')
print(df)
print('---------------------------------------------------------------------')
def cat_products(Quantity):
    if Quantity>10:
        return 'High Stock'
    elif Quantity>5:
        return 'Medium Stock'
    else:
        return 'Low Stock'
df['Stock_Status']=df['Quantity'].apply(cat_products)
print(df)
