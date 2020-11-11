# importing pandas package
import pandas as pd
 
# making data frame from csv file
data = pd.read_csv("nba.csv", index_col ="Name")
 
# retrieving columns by indexing operator
first = data["Age"]
 
 
 
print(first)
