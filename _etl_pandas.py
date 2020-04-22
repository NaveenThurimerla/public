import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/NaveenThurimerla/public/master/dummyemployee.csv")

print(df)   

headers = []

for row in df:
    
    headers.append(row)
    
keyvalue = pd.melt(df, id_vars=headers[0], value_vars=headers[1:])
print (keyvalue)
