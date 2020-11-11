import pandas as pd
import numpy as np
data = np.array(['a','b','c','d','e','f'])
s = pd.Series(data,index=[1000,1001,1002,1003,1004,1005])
print(s)
data = {'a' : 0., 'b' : 1., 'c' : 2.}
s = pd.Series(data,index=['b','c','d','a'])
print(s)
s = pd.Series(7, index=[0, 1, 2, 3])
print(s)
