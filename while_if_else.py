a=int(input("enter a number.\n"))
b=int(input("input a number.\n"))
c=a+b
print("DISPLAY...\n")
print(c)
if a>b:
    print("greater value:",a)
else:
  print("greater value->",b)
while a<=b:
    print(a,end=' ')
    if a>9:
        print("\n10 greater value.\n")
    a=a+1
