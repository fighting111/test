count = 3
password = 'hahaha'
while count:
    new_password = input('请输入密码...')
    if new_password == password:
        print('请稍等，马上进入程序...')
        break
    elif '*' in new_password:
        print('密码中不能包含*，您还有',count,'次输入机会')
    else:
        print('您还有',count-1,'次输入机会')
    count -= 1
