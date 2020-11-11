import pandas as pd
import numpy as np
data = np.array(['a','b','c','d','e','f'])
s = pd.Series(data)
 
 
# retrieve first three elements
print(s[:3])
data = np.array(['a','b','c','d','e','f'])
s = pd.Series(data)
 
 
# retrieve last three elements
print (s[-3:])
