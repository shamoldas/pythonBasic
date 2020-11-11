a=input("enter an integer number:")
b=input("enter an integer number:")
def intersect(a,b):
    res=[]
    for x in a:
        if x in b:
            res.append(x)
        return(res)
c=intersect(a,b)
print("apppend:",c)
