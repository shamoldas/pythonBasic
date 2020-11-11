# importing pandas module 
import pandas as pd 

# making data frame 
df = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv") 


df = pd.read_csv("nba.csv")  
df = pd.DataFrame(df)
a=df[['Name','Team','Number','Position','Age','College','Salary']]
print(a)
