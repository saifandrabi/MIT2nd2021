import pandas as pd
import numpy as np


d = {'Rollno' : pd.Series(np.arange(3), index=['i', 'ii', 'iii']),
   'marks': pd.Series([60,70,80,90], index=['i', 'ii', 'iii','iv'])}


df = pd.DataFrame(d)
print (df )#['one']
#Adding Column to exiting data frame
df['Grade+points']=pd.Series([10,20,30],index=['i', 'ii', 'iii'])
print (df )
