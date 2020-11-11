# importing pandas package 
import pandas as pd 

# making data frame from csv file 
df = pd.read_csv("nba.csv", index_col ="Name") 

print('First 10.\n')
a=df.head(10)

format_dict = {'Mes':'{:%m-%Y}'} #Simplified format dictionary with values that do make sense for our data
b=df.head().style.format(format_dict).highlight_max(color='darkgreen').highlight_min(color='#ff0000')
print(b)
