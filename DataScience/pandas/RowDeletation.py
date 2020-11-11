# importing pandas module 
import pandas as pd 

# making data frame from csv file 
data = pd.read_csv("nba.csv", index_col ="Name" ) 

# dropping passed values 
data.drop(["Avery Bradley", "John Holland", "R.J. Hunter", 
							"R.J. Hunter"], inplace = True) 

# display 
data
print(data)
