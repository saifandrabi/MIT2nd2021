import pandas as pd
import numpy as np

x=pd.Series(np.arange(10),index=[np.linspace(0,1,10)])

print(x)
data={ "age":['10-20','20-40','40-60'],
       "Cal Intake":[100,200,300]
       }
a=pd.DataFrame(data,index=[np.linspace(0,1,3)])

print(a)
print(a.loc[0])
Fi=pd.read_csv('/Users/syedmohsinsaif/Downloads/Affairs.csv')
print(Fi.to_string())
x=Fi.head(5)
print(x.to_string())