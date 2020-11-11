a=5
while a:
    print("a:",a,end=' ')
    a=a-1
    print("\ncheck_continue.\n")
    if a%2!=0:continue
    print(a,"odd\n",end=' ')
