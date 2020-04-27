import pandas as pd

#Read the data from CSV file
df = pd.read_csv("https://raw.githubusercontent.com/NaveenThurimerla/public/master/dummyemployee.csv")

#Printing the original String
print(df)   
#storing all the c
headers = df.columns

#Converting integer vvalues to string
df[df.columns[0]]=df[df.columns[0]].astype(str)

#Adding derived key to DataFrame
df['mainkey']=df[df.columns[0]]+'_'+df[df.columns[1]]
    
#unpivot the DataFrame
keyvalue = pd.melt(df, id_vars='mainkey', value_vars=headers[:])
print (keyvalue)
