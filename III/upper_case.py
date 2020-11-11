f=open('square.py')
while True:
    line=f.readline()
    if not line :
        break
    print(line.upper(),end=' ')
