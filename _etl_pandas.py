import pandas as pd

#Read the data from CSV file
df = pd.read_csv("https://raw.githubusercontent.com/NaveenThurimerla/public/master/dummyemployee.csv")

#Printing the original DF
print(df)   

#storing all the columns
headers = df.columns

#Converting  all the values to string
df=df[:].astype(str)

#Adding derived key to DataFrame
df['mainkey']=df[df.columns[0]]+'_'+df[df.columns[1]]
    
#unpivot the DataFrame
keyvalue = pd.melt(df, id_vars='mainkey', value_vars=headers[:])
print (keyvalue)
