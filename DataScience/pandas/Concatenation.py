# importing pandas module
import pandas as pd 
 
# Define a dictionary containing employee data 
data1 = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'], 
        'Age':[27, 24, 22, 32], 
        'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'], 
        'Qualification':['Msc', 'MA', 'MCA', 'Phd']} 
   
# Define a dictionary containing employee data 
data2 = {'Name':['Abhi', 'Ayushi', 'Dhiraj', 'Hitesh'], 
        'Age':[17, 14, 12, 52], 
        'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'], 
        'Qualification':['Btech', 'B.A', 'Bcom', 'B.hons']} 
 
# Convert the dictionary into DataFrame  
df = pd.DataFrame(data1,index=[0, 1, 2, 3])
 
# Convert the dictionary into DataFrame  
df1 = pd.DataFrame(data2, index=[4, 5, 6, 7])
 
print(df, "\n\n", df1)  
print('Concatetion.\n')
# using keys 
frames = [df, df1 ]
 
res = pd.concat(frames, keys=['x', 'y'])
res
print(res)
