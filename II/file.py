
f=open('data.txt','w')
f.write('hello\n')
s=input('enter a string.\n')
a=len(s)
print('string:',s)
print('length:',a)
print('upper:',s.upper())
f.close()
