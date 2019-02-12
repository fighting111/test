while True:
    num = input('请输入一个整数(输入Q结束程序)：')
    if num != 'Q':
        num = int(num)
        print('十进制 -> 十六进制：%d -> %x' % (num,num))
        print('十进制 -> 八进制：%d -> %o' % (num,num))
        print('十进制 -> 二进制：',num,'->',bin(num))
        #第二种print('十进制 -> 二进制：%d ->' % num,bin(num))
    else:
        break
