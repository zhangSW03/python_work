#根据用户名密码登录
is_True = True
count = 5
for i in range(1,6):
    username = input("请输入你的用户名:")
    pwd = input("请输入你的密码:")
    recount = count - i
    if username == "" or pwd == "":
        print("输入错误")
        continue

    if username == "admin" and pwd == "666888":
        print("登录成功！")
        break
    elif username == "zhangsan" and pwd == "123456":
        print("登录成功！")
        break
    elif username == "taoge" and pwd == "888666":
        print("登录成功！")
        break
    if recount == 0:
        print("输入错误五次，不允许在操作了")
        break