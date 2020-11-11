# import Pandas as pd 
import pandas as pd 

# create a new data frame 
df = pd.DataFrame({'Name': ['John Larter', 'Robert Junior', 'Jonny Depp'], 
				'Age':[32, 34, 36]}) 

print("Given Dataframe is :\n",df) 

# bydefault splitting is done on the basis of single space. 
print("\nSplitting 'Name' column into two different columns :\n", 
								df.Name.str.split(expand=True)) 




print('Check The first name & Last name.\n')
# create a new data frame 
df = pd.DataFrame({'Name': ['John Larter', 'Robert Junior', 'Jonny Depp'], 
                    'Age':[32, 34, 36]}) 
   
print("Given Dataframe is :\n",df) 
   
# Adding two new columns to the existing dataframe. 
# bydefault splitting is done on the basis of single space. 
df[['First','Last']] = df.Name.str.split(expand=True) 
   
print("\n After adding two new columns : \n", df) 
