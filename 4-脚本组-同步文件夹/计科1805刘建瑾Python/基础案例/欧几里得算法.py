# 模拟欧几里得算法(辗转相除法)
first_num = int(input('请输入第一个数:'))
second_num = int(input('请输入第一个数:'))
def Euclidean(first_num,second_num):
    while True:
        r = first_num % second_num
        first_num = second_num
        second_num = r
        if r == 0:
            print('这两个数之间的最大公约数是：',end='')
            break
    return first_num
print(Euclidean(first_num,second_num))

    
    
