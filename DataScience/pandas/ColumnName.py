# Import pandas package 
import pandas as pd 
	
# making data frame 
data = pd.read_csv("nba.csv") 

# iterating the columns 
for col in data.columns: 
	print(col) 
print("DataFrame Object.\n")

# list(data) or 
a=list(data.columns)
print(a)

print("Sorted")
s=sorted(data) 
print(s)
