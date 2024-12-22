# Create a DataFrame from a list of dictionaries
import pandas as pd
data=[
    {'Name':'Sura','Age':23,'City':'Novosibirsk'},
    {'Name':'Ivan','Age':24,'City':'Moscow'},
    {'Name':'Dmitry','Age':23,'City':'Petersburg'}
]
df=pd.DataFrame(data)
print(type(df))
print(df)