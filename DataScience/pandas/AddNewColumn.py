# Import pandas package 
import pandas as pd 

# Define a dictionary containing Students data 
data = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'], 
		'Height': [5.1, 6.2, 5.1, 5.2], 
		'Qualification': ['Msc', 'MA', 'Msc', 'Msc']} 

# Convert the dictionary into DataFrame 
df = pd.DataFrame(data) 

# Using DataFrame.insert() to add a column 
df.insert(2, "Age", [21, 23, 24, 21], True) 

# Observe the result 
df 
print(df)

# Define a dictionary containing Students data 
data = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'], 
        'Height': [5.1, 6.2, 5.1, 5.2], 
        'Qualification': ['Msc', 'MA', 'Msc', 'Msc']} 
  
# Convert the dictionary into DataFrame 
df = pd.DataFrame(data) 
  
# Declare a list that is to be converted into a column 
address = ['Delhi', 'Bangalore', 'Chennai', 'Patna'] 
  
# Using 'Address' as the column name 
# and equating it to the list 
df['Address'] = address 
  
# Observe the result 
df
print(df)



# Define a dictionary containing Students data 
data = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'], 
        'Height': [5.1, 6.2, 5.1, 5.2], 
        'Qualification': ['Msc', 'MA', 'Msc', 'Msc']} 
   
   
# Convert the dictionary into DataFrame 
df = pd.DataFrame(data) 
  
# Using 'Address' as the column name and equating it to the list 
df2 = df.assign(address = ['Delhi', 'Bangalore', 'Chennai', 'Patna']) 
   
# Observe the result 
df2 



print(df2)

