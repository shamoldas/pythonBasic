# importing pandas package 
import pandas as pd 

# making data frame from csv file 
data = pd.read_csv("nba.csv", index_col ="Team") 

# retrieving rows by loc method 
rows = data.loc["Utah Jazz"] 

# checking data type of rows 
print(type(rows)) 

# display 
rows 
print(rows)
