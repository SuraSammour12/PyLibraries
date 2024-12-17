# Pandas Series Temprature Example
import pandas as pd
temp=pd.Series([15,14,16,18,15,14,14],index=['Sat','Sun','Mon','Tue','Wed','Thu','Fri'])
print(temp)
# calculate the average temperature
avg_temp=temp.mean()
print(f"Average Temperature is {avg_temp}")