a=int(input("enter a loop 1st number.\n"))
b=int(input("input last number.\n"))
a=b//2
while a>1:
    print("\na:",a,end=' ')
    if b % a ==0:
        print(b,"has_factor",a)
        break
    a=a-1
    
else:
        print(b,"is_prime.\n")
