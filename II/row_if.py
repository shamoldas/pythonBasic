m=[[1,2,3],[4,5,6],[7,8,9]]
col2=[row[1] for row in m]
print('colom 2:',col2)
a=[row[1] for row in m if row[1]%2==0]
print('divide by 2:',a)
