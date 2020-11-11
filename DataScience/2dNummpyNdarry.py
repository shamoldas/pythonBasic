# Program to create DataFrame from 2D array 
import pandas as pd # Import Library 
d1 =[[2, 3, 4], [5, 6, 7]] # Define 2d array 1 
d2 =[[2, 4, 8], [1, 3, 9]] # Define 2d array 2 
Data ={'first': d1, 'second': d2} # Define Data 
df2d = pd.DataFrame(Data) # Create DataFrame 
print(df2d)
