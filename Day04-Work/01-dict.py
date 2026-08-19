#学生管理系统-字典
menu = """
# # # # # # # # # # # # # # # # # # # # # # # 【图书管理系统菜单】 # # # # # # # # # # # # # # # # # #
#       1. 添加图书  2. 修改图书  3. 删除图书  4. 查询图书  5. 列出所有图书  6. 图书统计  7. 退出系统        #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""
print("欢迎使用图书管理系统 ~")

book_dict = {}
while True:
    print(menu)

    operate = input("请选择你要执行的操作:")
    match operate:
        case "1":
            book_id = int(input("请输入你的图书序号:"))
            if book_id in book_dict:
                print("该序号已有书占用，请重新输出:")
                continue
            else:
                book_name = input("请输入你的图书名称:")
                book_author = input("请输入图书的作者:")
                book_price = float(input("请输入图书的价格:"))
                book_num = int(input("请输入图书的库存数量:"))

                book_dict[book_id] = {'book_name':book_name, 'book_author':book_author, 'book_price':book_price, 'book_num':book_num}
        case "2":
            book_id = int(input("请输你要修改的图书序号:"))
            if book_id in book_dict:
                book_name = input("请输入修改后的图书名称:")
                book_author = input("请输入修改后的图书作者:")
                book_price = float(input("请输入修改后的图书价格:"))
                book_num = int(input("请输修改后的图书数量:"))
                book_dict[book_id] = {'book_name':book_name, 'book_author':book_author, 'book_price':book_price, 'book_num':book_num}
            else:
                print("未能找到该本书，无法进行修改操作.")
        case "3":
            book_id = int(input("请输你要修改的图书序号:"))
            if book_id in book_dict:
                del book_dict[book_id]
            else:
                print("未能找到该本书，无法进行删除操作.")
        case "4":
            book_id = int(input("请输你要修改的图书序号:"))
            if book_id in book_dict:
                print(f"书的名称为:{book_dict[book_id]['book_name']},作者是:{book_dict[book_id]['book_author']},单价是:{book_dict[book_id]['book_price']}元,库存剩余:{book_dict[book_id]['book_num']}本")
            else:
                print("未能找到该本书，无法进行查询操作.")
        case "5":
            if len(book_dict) == 0:
                print("图书管理系统内无图书信息")
            else:
                for key, value in book_dict.items():
                    print(f"图书的名称为:{value['book_name']},作者是:{value['book_author']},单价是:{value['book_price']}元,库存剩余:{value['book_num']}本")
        case "6":
            total_book = len(book_dict)
            if total_book == 0:
                print("图书管理系统内无图书信息")
            else:
                total_num = 0
                total_price = 0

                price = []
                for key, value in book_dict.items():
                    total_num += value['book_num']
                    total_price += value['book_price'] * value['book_num']
                    price.append(value['book_price'])

                max_price = max(price)
                min_price = min(price)

                max_book_price = [value for id, value in book_dict.items() if value['book_price']==max_price]
                min_book_price = [value for id, value in book_dict.items() if value['book_price']==min_price]

                print("===== 图书统计 =====")
                print(f"图书种类总数: {total_book}")
                print(f"库存总量: {total_num}本")
                print(f"总价值: {total_price:.2f}元")
                print(f"价格最高: {max_price:.2f}元,图书的名称是:{max_book_price[0]['book_name']}")
                print(f"价格最低: {min_price:.2f}元,图书的名称是:{min_book_price[0]['book_name']}")
        case "7":
            print("退出操作")
            break
        case _:
            print("无该项操作,请重新选择")
            continue

