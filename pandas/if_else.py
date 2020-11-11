import pandas as pd
import numpy as np
 
df1 = {
    'State':['Arizona AZ','Georgia GG','Newyork NY','Indiana IN','Florida FL'],
   'Score':[4,47,55,74,31]

    }
df1['Grade'] = np.where(df1['Score'] >=40, 'Pass','Fail')
 
df1 = pd.DataFrame(df1,columns=['State','Score'])
print(df1)
#df1['Grade'] = np.where(df1['Score'] >=70, 'Distinction',df1['Grade'])

