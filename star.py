n=int(input("the number of rows="))
for i in range(0,n):
    for j in range (i):
        print(' ',end='')
    for k in range(i,n):
        print('*',end='')
    print()
for i in range(n-1,-1,-1):
    for j in range(0,i):
        print(' ',end='')
    for k in range(i,n):
        print('*',end='')
    print()
