
for i in range (1):
        print(i+1,'check')
        
a=int(input('enter a integer value.\nfor for loop.\n'))
for i in range(a):
            print(i+1,'shamol')
print('finished.\n')
s=input('enter a string.\n continuesly moving the character.\n')
for i in range(len(s)):
               s=s[1:]+s[:1]
               print(s,end=' ')
print('\ncool')
