# Task :DataFrame
import pandas as pd
lst = [
    {'Product':'Sweater','Price': 35,'Quantity': 20,'Discount': 5},
    {'Product':'Jacket','Price': 60,'Quantity': 15,'Discount': 20},
    {'Product':'Coffee Mug','Price': 10,'Quantity': 100,'Discount': 5},
    {'Product':'Glass Cup','Price': 12,'Quantity': 60,'Discount': 15}
]
df=pd.DataFrame(lst)
print(df)

# Task : find median of discount column
median_discount=df['Discount'].median()
print(median_discount)