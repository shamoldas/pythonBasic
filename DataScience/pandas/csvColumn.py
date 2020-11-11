


# importing pandas module 
import pandas as pd 
  
# making data frame from csv file 
data = pd.read_csv("nba.csv", index_col ="Name" ) 

print(data)
