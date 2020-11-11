# Python code to demonstrate 
# del and assert 

# initialising list 
a = [1, 2, 3] 

# printing list before deleting any value 
print ("The list before deleting any value") 
print (a) 

# using del to delete 2nd element of list 
del a[1] 

# printing list after deleting 2nd element 
print ("The list after deleting 2nd element") 
print (a) 

# demonstrating use of assert 
# prints AssertionError 
assert 5 > 3, "5 is greater than 3"
# prints AssertionError 
assert 5 < 3, "5 is not smaller than 3"
