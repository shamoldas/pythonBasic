import numpy as np
from scipy import linalg 

A = np.array([[1,2,3],[4,5,6],[7,8,8]])
linalg.det(A) 

P, L, U = linalg.lu(A) 
print(P) 
print(L) 
print(U) 
# print LU decomposition 
print(np.dot(L,U)) 


eigen_values, eigen_vectors = linalg.eig(A) 
print(eigen_values) 
print(eigen_vectors) 


v = np.array([[2],[3],[5]]) 
print(v) 
s = linalg.solve(A,v) 
print(s) 
