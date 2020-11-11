a=int(input("enter a number.\nthe number less than 10.\n"))
b=int(input("input a number.\n"))
c=a+b
print("DISPLAY...\n")
print('sum',c)
while a<=b:
   # print(a,end=' ')
    a=a+1
    if a%2==0:
        print("even: ",a)
    else:
        print("odd: ",a)
