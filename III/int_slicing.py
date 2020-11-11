
print('hmm')
s=input("enter a string.\n")
for item in s:
    print(item,end=' ')
s=[1,2,3,4,5]
for i in range(len(s)):
    x=s[i:]+s[:i]
    print(x,end=' ')
