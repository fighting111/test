# 使用‘除2取余’法,模拟十进制转二进制的函数bin()
num = int(input('请输入一个数字：'))
def Binary(num):
    temp = []
    result = ''
    while num:  #这里尽量不要用True，没意义，循环不停，不必要错误
        r = num % 2
        num = num // 2  #必须先弄余数，否则num改变
        temp.append(r)
        result += str(temp.pop())  #pop从末尾删除
    print('0b',end='')
    return result
print(Binary(num))

#程序有bug。。。。
    
