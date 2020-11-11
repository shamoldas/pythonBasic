# importing pandas module
import pandas as pd 
 
# Define a dictionary containing employee data 
data1 = {'key': ['K0', 'K1', 'K2', 'K3'],
         'key1': ['K0', 'K1', 'K0', 'K1'],
         'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'], 
        'Age':[27, 24, 22, 32],} 
   
# Define a dictionary containing employee data 
data2 = {'key': ['K0', 'K1', 'K2', 'K3'],
         'key1': ['K0', 'K0', 'K0', 'K0'],
         'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'], 
        'Qualification':['Btech', 'B.A', 'Bcom', 'B.hons']} 
 
# Convert the dictionary into DataFrame  
df = pd.DataFrame(data1)
 
# Convert the dictionary into DataFrame  
df1 = pd.DataFrame(data2) 
  
 
print(df, "\n\n", df1) 
res1 = pd.merge(df, df1, on=['key', 'key1'])
 
res1
print(res1)

print('Left Frame.\n')

# using keys from left frame
res = pd.merge(df, df1, how='left', on=['key', 'key1'])
 
res
print(res)

print('Right.\n')
# using keys from right frame
res1 = pd.merge(df, df1, how='right', on=['key', 'key1'])

print(res1)

print('Outer.\n')
# getting union  of keys
res2 = pd.merge(df, df1, how='outer', on=['key', 'key1'])
 
res2
print(res2)
