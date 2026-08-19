a = int(input("请你输入一个月份："))

match a :
    case 3|4|5:
        print("你输入的月份是春季")
    case 6|7|8:
        print("你输入的月份是夏季")
    case 9|10|11:
        print("你输入的月份是秋季")
    case 12|1|2:
        print("你输入的月份是冬季")
    case _:
        print("月份输入有误")