
# importing pandas 
import pandas as pd 
  
df = pd.DataFrame({'Last': ['Gaitonde', 'Singh', 'Mathur'], 
                   'First': ['Ganesh', 'Sartaj', 'Anjali']}) 
  
print('Before Join') 
print(df, '\n') 
  
print('After join') 
df['Name'] = df['First'].str.cat(df['Last'], sep =" ") 
print(df) 
