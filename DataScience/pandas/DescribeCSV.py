# importing pandas package 
import pandas as pd 

# making data frame from csv file 
data = pd.read_csv("nba.csv", index_col ="Name") 

print('First 10.\n')
a=data.head(10)
print(a)

print('Dscribe.\n')

d=data.describe()

print(d)

print('Info')

b=data.info()
print(b)
