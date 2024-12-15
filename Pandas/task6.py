#Task-6:
import pandas as pd
data=[
     {'Product': 'Laptop', 'Price': 1200, 'Quantity': 5, 'Discount': 10},
    {'Product': 'Tablet', 'Price': 600, 'Quantity': 10, 'Discount': 15},
    {'Product': 'Smartphone', 'Price': 800, 'Quantity': 7, 'Discount': 5},
    {'Product': 'Monitor', 'Price': 300, 'Quantity': 12, 'Discount': 20}
]
df=pd.DataFrame(data)
print(df)
print("-----------------------------------------------------------------------")
#Filtering Data
filtered_data=df[(df['Price']>=800)&(df['Quantity']>=5)]
print(filtered_data)