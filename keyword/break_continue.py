# Function to illustrate break in loop 
def breakTest(arr): 
	for i in arr: 
		if i == 5: 
			break
		print (i) 
	# For new line 
	print


# Function to illustrate continue in loop 
def continueTest(arr): 
	for i in arr: 
		if i == 5: 
			continue
		print (i) 

	# For new line 
	print

# Function to illustrate pass 
def passTest(arr): 
		pass

	
# Driver program to test above functions 

# Array to be used for above functions: 
arr = [1, 3 , 4, 5, 6 , 7] 

# Illustrate break 
print ("Break method output")
breakTest(arr) 

# Illustrate continue 
print ("Continue method output")
continueTest(arr) 

# Illustrate pass- Does nothing 
passTest(arr) 

