# importing pandas module 
import pandas as pd 
	
# making data frame 
df = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv") 

a=df.head(10)
print(a)
df = pd.read_csv("nba.csv")  
  
# five largest values in column age 
a=df.nlargest(5, ['Age'])
print(a)
print('\n Maximum salary')
s=df.nlargest(5, ['Salary'])

print(s)

