import random
time = 0
answer = random.randint (1,10)
print('猜字谜')
guess = 0
#print()默认是打印完字符串会自动添加一个换行符，end=" "参数告诉print()用空格代替换行
print ('猜猜我心里想的是什么数字？', end = ' ')
while (guess != answer) and (time < 3):
    guess = int (input ())
    time += 1 #每输入一次，可用机会就-1
    if guess == answer:#是guess作第一个if条件～
        print('wtf,你是我心里的蛔虫吗？')
    else:
        if guess > secret:
            print('大了大了！！')
        else:
            print('小了小了！！')
        if time < 3 :
            print ('再试一次吧：', end = ' ')
        else:
            print('机会用完了，退下吧。')
print('游戏结束，又被坑了吧！！')
