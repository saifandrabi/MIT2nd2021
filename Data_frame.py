import pandas as pd
import numpy as np

data = {
  "Subject": ['C', 'OS', 'Java',"os"],
  "Marks": ['50', 40, 45,100]
}

#load data into a DataFrame object:
df = pd.DataFrame(data)

print(df)
#Accessing Row 2 and Row 3
print(df.loc[[0,2,3]])
# Creating another Dataframe
data={ "age":['10-20','20-40','40-60'],
       "Cal Intake":[100,200,300]
       }
# using Linespace to create Index
a=pd.DataFrame(data,index=[np.linspace(0,1,3)])

print(a)
#Accesing a particular Row
print(a.loc[0])
# Reading a particulat File
Fi=pd.read_csv('/Users/syedmohsinsaif/Downloads/Affairs.csv')
# to print the file read
print(Fi.to_string())
#displaying first 5 rows of dataframe
x=Fi.head(5)
print(x.to_string())
#displaying Tail
y=Fi.tail(50)
print(y)