temp = input('请输入一个年份：')
while not temp.isdigit():
    temp = input("抱歉，您的输入有误，请输入一个整数：")

year = int(temp)
if year/400 == int(year/400):#世纪闰年【类似%取余的操作】
    print(temp + ' 是闰年！')
else:#普通闰年
    if (year/4 == int(year/4)) and (year/100 != int(year/100)):
        print(temp + ' 是闰年！')
    else:
       print(temp + ' 不是闰年！')
