# importing pandas as pd 
import pandas as pd 

# sample dataframe 
df = pd.DataFrame({'A': ['foo', 'bar', 'g2g', 'g2g', 'g2g', 
						'bar', 'bar', 'foo', 'bar'], 
				'B': ['a', 'b', 'a', 'b', 'b', 'b', 'a', 'a', 'b'] }) 

# frequency count of column A 
count = df['A'].value_counts() 
print(count) 

print('Using GroupBy Count')

# sample dataframe 
df = pd.DataFrame({ 'A': ['foo', 'bar', 'g2g', 'g2g', 'g2g', 
                                'bar', 'bar', 'foo', 'bar'], 
                   'B': ['a', 'b', 'a', 'b', 'b', 'b', 'a', 'a', 'b'] }) 
  
# Multi-column frequency count 
count = df.groupby(['A']).count() 
print(count) 

print('GroupBy Size.\n')

# sample dataframe 
df = pd.DataFrame({ 'A': ['foo', 'bar', 'g2g', 'g2g', 'g2g',  
                                'bar', 'bar', 'foo', 'bar'], 
                   'B': ['a', 'b', 'a', 'b', 'b', 'b', 'a', 'a', 'b'] }) 
  
# Multi-column frequency count 
count = df.groupby(['A', 'B']).size() 
print(count) 
