#密码安全性检查代码
symbols = r''':~`!@#$%^&*()_=-/,'".?\<>;:[]{}|'''
#这里注意特殊字符不要把转义符放在末尾，防止误判
letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
nums = '0123456789'
password = input('请输入设定好的密码...')
length = len(password)
while (password.isspace() or length == 0):  #假定用户未输入密码...
    password = input('您输入的密码为空，请重新输入...') #这里不能使用print函数，因为需要用户继续输入密码
#判断长度
if length < 8:
    flag_len = 1
elif 8 <= length < 16:
    flag_len = 2
else:
    flag_len = 3
    
count = 0
#判断是否包含特殊字符
for each in password:
    if each in symbols:
        count += 1       #这样减少判断含有几个特殊字符的次数，循环自动帮忙
        break       #break意味着跳出循环体
#判断是否包含字母
for each in password:
    if each in letters:
        count +=1
        break
#判断是否包含数字
for each in password:
    if each in nums:
        count +=1
        break
while True:
    print('您的密码安全等级评定为：',end='')
    if (flag_len == 1 or count == 1):
        print('低')
    elif (flag_len == 2 or count == 2):
        print('中')
    else:
        password = list(password)   #判断用户输入密码是否以字母开头
        if password[0] in letters:
            print('高')
            print('请继续保持！')
            break  #这里break意味着跳出循环体
        else:
            print('中')
    print('''请按以下方式提高您的密码安全等级：
     \t1、密码必须由数字、字母及特殊字符三种组合
     \t2、密码必须由字母开头
     \t3、密码长度不低于16位。''')  #这里将低级和中级需要出现的内容写到一起/多行文字
    break
    

#低级密码要求：
#1、密码由单纯的数字或字母组成
#2、密码长度小于等于8位

#中级密码要求：
#1、密码必须由数字、字母或特殊字符(权限:~!@#$%^&*()_=-/,.?<>;:[]{}|\)任意两种组合
#2、密码长度不能低于8位

#高级密码要求：
#1、密码必须由数字、字母或特殊字符(权限:~!@#$%^&*()_=-/,.?<>;:[]{}|\)任意三种组合
#2、密码只能由字母开头
#3、密码长度不能低于16位












