a=int(input("enter an integer number:"))
b=int(input("enter an integer number:"))
def addition(a,b):
    return(a+b)
def subtraction(a,b):
    return(a-b)
def multiplication(a,b):
    return(a*b)
def division(a,b):
    if b==0:
        return"undefine"
    else :
        return(a/b)
x=addition(a,b)
y=subtraction(a,b)
z=multiplication(a,b)
q=division(a,b)
print("addition:",x,"\nsubtraction:",y,"\nmultiplication:",z,"\ndivision:",q)
print(addition)
