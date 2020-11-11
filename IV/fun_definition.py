def intersect(a,b):
    res=[]
    for x in a:
        if x in b:
            res.append(a)
    return(res)
a=input('enter a string.\n')
b=input('enter the second string.\n')
print('multi:',func(a,b))
