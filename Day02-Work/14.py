#模拟银行取款机
start = 10000

while True:
    print("=======银行取款机=======")
    print("1.查询余额")
    print("2.存款")
    print("3.取款")
    print("4.退出")

    fun = int(input("请输入你的操作:"))
    if fun == 1:
        print(f"你的余额为{start}")
        break
    if fun == 2:
        money = float(input("请输入你的存款金额："))
        if money >= 0:
            start = start+money
            print(f"你的存款金额为{money}元,余额还剩余{start}元")
            break
        else:
            print("存款金额错误")
    if fun == 3:
        money1 = float(input("请输入你的取款金额："))
        if money1 <= 0:
            print("取款金额错误")
        elif money1 > start:
            print(f"余额不足!当前余额:{start:.2f}")
        else:
            start = start - money1
            print(f"你的取款金额为{money1}元,余额还剩余{start}元")
    if fun == 4:
        print("感谢使用")
        break
    else:
        print("请重新选择")
        continue