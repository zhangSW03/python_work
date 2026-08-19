#简易计算器
while True:
    num1 = float(input("请你输入第一个数："))
    num2 = float(input("请你输入第二个数："))
    operator = input("请你输入你的运算符：")


    match operator:
        case "+":
            print(f"{num1} + {num2} = {num1 + num2}")
        case "-":
            print(f"{num1} - {num2} = {num1 - num2}")
        case "*":
            print(f"{num1} * {num2} = {num1 * num2}")
        case "/":
            if num2 == 0:
                print("除数不能为零")
            else:
                res = num1 / num2
                print(f"{num1} / {num2} = {num1 / num2}")
        case _:
            print("运算符不匹配")

    choice = input("是否继续计算？(Y/N)")
    if choice == "N" or choice == "n":
        print("退出")
        break
    elif choice != "Y" and choice != "y":
        print("输入无效")
        break