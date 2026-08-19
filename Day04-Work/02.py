#商品库存管理系统
from operator import index

menu = """
# # # # # # # # # # # # # # # # # # # # # # # # 【商品库存管理系统菜单】 # # # # # # # # # # # # # # # # # # # # # # #
#                 1.添加商品  2.修改商品  3.删除商品  4.查询商品  5.列出所有商品  6.库存统计  7.退出系统                  #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""
print("欢迎使用商品库存管理系统 ~")
commodities = []
# 库存预警阈值：库存低于此值会提示
WARNING_STOCK = 10

while True:
    print(menu)
    option = int(input("请选择要执行的操作(1~7):"))
    if option == 1:
        name = input("请输入商品名称:")
        category = input("请输入商品分类:")
        price = float(input("请输入商品单价:"))
        num = int(input("请输入商品数量:"))
        if price<=0 or num <0:
            print("请输入正确数值")
        else:
            commodities.append({"name": name, "category": category, "price": price, "num": num})
            print("添加成功")

    elif option == 2:
        new_name = input("请输入你要修改的商品名称:")
        for commodity in commodities:
            if commodity["name"] == new_name:
                category = input("请输入修改的商品的类别:")
                price = float(input("请输入修改的商品的单价:"))
                num = int(input("请输入修改的商品的库存数量:"))
                if price<=0 or num <0:
                    print("请输入修改后正确的值")
                else:
                    commodity["num"] = num
                    commodity["price"] = price
                    commodity["category"] = category
                    print("修改成功")
                    break
        else:
            print("未找到该商品")
    elif option == 3:
        name=input("请输入要删除的商品名称:")
        for commodity in commodities:
            if commodity["name"] == name:
                del commodities[commodities.index(commodity)]
                print("删除成功")
                break
        else:
            print("未找到该商品")
    elif option == 4:
        name=input("请输入要查询的商品名称:")
        for commodity in commodities:
            if commodity["name"] == name:
                print(f"商品名称{commodity['name']},商品的分类:{commodity['category']},商品的单价:{commodity['price']}元,库存数量:{commodity['num']}")
                break
        else:
            print("未找到该商品")
    elif option == 5:
        if len(commodities) <= 0:
            print("商品未有库存")
        else:
            for commodity in commodities:
                print(f"商品的名称:{commodity['name']},分类:{commodity['category']},单价:{commodity['price']}元,库存数量:{commodity['num']}")
    elif option == 6:
        if len(commodities) <= 0:
            print("商品未有库存")
        else:
            total_num = 0
            total_price = 0
            low_list = []
            max_price = commodities[0]
            min_price = commodities[0]
            total_commodity = len(commodities)
            for commodity in commodities:
                price = commodity["price"]
                num = commodity["num"]

                total_num += num
                total_price += price * num

                if max_price["price"] < commodity["price"]:
                    max_price = commodity
                if min_price["price"] > commodity["price"]:
                    min_price = commodity

                if commodity['num'] < WARNING_STOCK:
                    low_list.append(commodity)
            print('=======库存统计=======')
            print(f"商品种类一共:{total_commodity}个")
            print(f"商品的库存总量为:{total_num}")
            print(f"商品总价值为:{total_price}")
            print(f"{max_price['name']}的单价最高,单价{max_price['price']}")
            print(f"{min_price['name']}的单价最低,单价{min_price['price']}")
            print('=====库存不足商品=====')
            if len(low_list) == 0:
                print("暂无库存不足的商品")
            else:
                for commodity in low_list:
                    print(f"商品名称:{commodity['name']},单价:{commodity['price']},库存剩余:{commodity['num']}")

    elif option == 7:
        print("退出系统")
        break
    else:
        print("很抱歉，该系统没有此项操作")
        break

