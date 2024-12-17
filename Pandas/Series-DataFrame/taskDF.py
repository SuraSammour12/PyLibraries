#Task-2:DataFrame
import pandas as pd
lst = [
    {'Product':'Sweater','Price': 35,'Quantity': 20,'Discount': 5},
    {'Product':'Jacket','Price': 60,'Quantity': 15,'Discount': 20},
    {'Product':'Coffee Mug','Price': 10,'Quantity': 100,'Discount': 5},
    {'Product':'Glass Cup','Price': 12,'Quantity': 60,'Discount': 15},
     {'Product':'Shirt','Price': 25,'Quantity': 50,'Discount': 5}
]
df=pd.DataFrame(lst)
print(df)
print("-----------------------------------------------------------------")
#Task-3:find median of discount column
median_discount=df['Discount'].median()
print(f"median discount is : {median_discount}")
print("-----------------------------------------------------------------")
#Task-4:
product=df['Product']
print(product)
print("-----------------------------------------------------------------")
subset=df[['Price','Discount']]
print(subset)
print("-----------------------------------------------------------------")
#Task-5:
first_two_rows=df.iloc[0:2]
last_two_rows=df.iloc[-2:]
print(first_two_rows)
print(last_two_rows)
print("-----------------------------------------------------------------")
new_df=df.set_index('Product')
print(new_df)
print("-----------------------------------------------------------------")
product=new_df.loc['Sweater']
print(product)
