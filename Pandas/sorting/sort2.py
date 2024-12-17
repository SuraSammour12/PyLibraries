import pandas as pd
sales_data = {
    'Product': ['Laptop', 'Headphones', 'Keyboard', 'Mouse'],
    'Units Sold': [150, 300, 200, 250],
    'Date': pd.to_datetime(['2024-01-15', '2024-01-10', '2024-01-12', '2024-01-14'])
}
# Note: pd.to_datetime converts string dates into datetime objects, 
# allowing easier date manipulation, filtering, and analysis.
sales_df=pd.DataFrame(sales_data)
print(sales_df)
print('-----------------------------------------------------------------')
# sort by units Sold in descending order to find top-selling products
top_selling=sales_df.sort_values(by='Units Sold',ascending=False)
print(top_selling)
print('-----------------------------------------------------------------')
top_selling.reset_index(drop=True,inplace=True)
print(top_selling)