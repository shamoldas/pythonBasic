# importing libraries
import numpy as np
 
# sort along the first axis
a = np.array([[12, 15], [10, 1]])
arr1 = np.sort(a, axis = 0)        
print ("Along first axis : \n", arr1)        
 
 
# sort along the last axis
a = np.array([[10, 15], [12, 1]])
arr2 = np.sort(a, axis = -1)        
print ("\nAlong first axis : \n", arr2)
 
 
a = np.array([[12, 15], [10, 1]])
arr1 = np.sort(a, axis = None)        
print ("\nAlong none axis : \n", arr1)
