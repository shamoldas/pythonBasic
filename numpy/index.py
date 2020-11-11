# Python program to demonstrate 
# the use of index arrays.
import numpy as np
 
# Create a sequence of integers from
# 10 to 1 with a step of -2
a = np.arange(10, 1, -2) 
print("\n A sequential array with a negative step: \n",a)
 
# Indexes are specified inside the np.array method.
newarr = a[np.array([3, 1, 2 ])]
print("\n Elements at these indices are:\n",newarr)
# Arrange elements from 0 to 19
a = np.arange(20)
print("\n Array is:\n ",a)
 
# a[start:stop:step]
print("\n a[-8:17:1]  = ",a[-8:17:1]) 
 
# The : operator means all elements till the end.
print("\n a[10:]  = ",a[10:])
