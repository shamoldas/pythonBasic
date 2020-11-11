a=int(input("enter a number.\n"))
b=int(input("input a number.\n"))
c=a+b
print("DISPLAY...\n")
print('sum',c)
while a<=b:
   # print(a,end=' ')
    a=a+1
    if a%2==0:
        print("even: ",a)
        even_sum=even_sum+a;
    else:
        print("odd: ",a)
        odd_sum=odd_sum+a;

print('sum even:',even_sum)
print('sum_odd:',odd_sum)
