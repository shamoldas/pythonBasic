a=int(input('enter a integer number.\n')
def maker(a):
      return lambda x:x**a
p=maker(a)
print('a:',p)
