import pandas as pd
import numpy as np
 
#Create a DataFrame
df1 = {
    'Name':['George','Andrea','micheal','maggie','Ravi','Xien','Jalpa',np.nan],
    'State':['Arizona','Georgia','Newyork','Indiana','Florida','California',np.nan,np.nan],
    'Gender':["M","F","M","F","M","M",np.nan,np.nan],      
    'Score':[63,48,56,75,np.nan,77,np.nan,np.nan]
     
   }
 
df1 = pd.DataFrame(df1,columns=['Name','State','Gender','Score'])
df1.notnull().sum()
print(df1)
print(df1.notnull().sum())
#print(df1)
print(df1.Score.notnull().sum())
