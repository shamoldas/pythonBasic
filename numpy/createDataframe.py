# Python code demonstrate creating 
# DataFrame from dict narray / lists 
# By default addresses. 

import pandas as pd 

# intialise data of lists. 
data = {'Name':['Tom', 'nick', 'krish', 'jack'], 'Age':[20, 21, 19, 18]} 

# Create DataFrame 
df = pd.DataFrame(data) 

# Print the output. 
print(df) 

# dictionary of lists 
dict = {'name':["aparna", "pankaj", "sudhir", "Geeku"], 
        'degree': ["MBA", "BCA", "M.Tech", "MBA"], 
        'score':[90, 40, 80, 98]} 
  
df = pd.DataFrame(dict) 
  
print(df)
