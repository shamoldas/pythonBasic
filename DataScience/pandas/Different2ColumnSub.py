import pandas as pd 

# Create a DataFrame 
df1 = { 'Name':['George','Andrea','micheal', 
				'maggie','Ravi','Xien','Jalpa'], 
		'score1':[62,47,55,74,32,77,86], 
		'score2':[45,78,44,89,66,49,72]} 

df1 = pd.DataFrame(df1,columns= ['Name','score1','score2']) 

print("Given Dataframe :\n", df1) 

df1['Score_diff'] = df1['score1'].sub(df1['score2'], axis = 0) 
print("\nDifference of score1 and score2 :\n", df1) 
