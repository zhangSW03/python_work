#判断用户输入的数
n = int(input("请输入一个整数："))
# if n >0 and n % 2 == 0:
#     print(f"你输入的数字{n},属于正偶数")
# elif n >0 and n % 2 == 1:
#     print(f"你输入的数字{n},属于正奇数")
# elif n < 0 and n % 2 == 0:
#     print(f"你输入的数字{n},属于负偶数")
# elif n < 0 and n % 2 == 1:
#     print(f"你输入的数字{n},属于负奇数")
# else:
#     print("零")

match n:
    case _ if n > 0 and n % 2 == 0:
        print(f"你输入的数字{n},属于正偶数")
    case _ if n > 0 and n % 2 != 0:
        print(f"你输入的数字{n},属于正奇数")
    case _ if n < 0 and n % 2 == 0:
        print(f"你输入的数字{n},属于负偶数")
    case _ if n < 0 and n % 2 != 0:
        print(f"你输入的数字{n},属于负奇数")
    case _:
        print("零")
