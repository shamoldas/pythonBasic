p=['a','e','i','o','u']
q=['A','E','I','O','U']
s=[1,2,3,4,5]
r=[6,7,8,9,0]

for (x,y,z,a)in list(zip(s,r,p,q)):
    print(x,y,' = ',x+y,'-',z,'-',a)
