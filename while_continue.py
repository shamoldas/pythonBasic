a=int(input("enter a loop 1st number.\n"))
b=int(input("input last number.\n"))
while a<=b:
    print(a,end=' ')
    a=a+1
    print("\ncheck_continue.\n")
    if a%2!=0:continue
    print(a,"check",end=' ')
