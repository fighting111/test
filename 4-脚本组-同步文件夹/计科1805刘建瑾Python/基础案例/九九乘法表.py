#第一种方法：
for i in range(1,10):
    for j in range(1,i+1):
        print('{}x{}={}'.format(j,i,i*j),end=' ')
    print()

#第二种方法：
for i in range(1,10):
    for j in range(1,i+1):
        n = i * j
        print(i,'*',j,'=',n,end='   ‘)
    print()
    
#第三种方法：
for i in range(1, 10):
    for j in range(1, i+1):
        print("%d*%d=%d\t" % (j, i, i*j), end="")
    print()
              
