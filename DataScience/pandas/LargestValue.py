# importing pandas module 
import pandas as pd 
	
# making data frame 
df = pd.read_csv("nba.csv") 

# five largest values in column age 
a=df.nlargest(5, ['Age'])
print(a)
