import pandas as pd
# Create a DataFrame from a dictionary of lists
dictionary={
    'Name':['sura','sally','victor'],
    'Age':['23Y','3M','1.5Y'],
    'City':['Tulkarm','Nablus','Tulkarm']
}
df=pd.DataFrame(dictionary)
print(type(df))
print(df)