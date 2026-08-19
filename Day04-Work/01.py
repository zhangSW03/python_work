#图书管理系统
print("欢迎使用图书管理系统 ~")
books = []
while True:
    print(" # # # # # # # # # # # # # # # # # # # # # # # 【图书管理系统菜单】 # # # # # # # # # # # # # # # # # #")
    print("#       1. 添加图书  2. 修改图书  3. 删除图书  4. 查询图书  5. 列出所有图书  6. 图书统计  7. 退出系统         #")
    print(" # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #")

    option = int(input("请输入你的操作:"))
    if option == 1:
        name = input("请输入图书名称：")
        author = input("请输入图书作者：")
        price = float(input("请输入图书价格："))
        stock = int(input("请输入库存数量："))
        if price <=0 or stock <0:
            print("请输入正确的值")
        else:
            book = {"name": name, "author": author, "price": price,"stock": stock}
            books.append(book)
            print("图书添加成功")
    elif option == 2:
        name = input("请输入要修改的图书名称：")
        for book in books:
            if book["name"] == name:
                new_author = input("请输入要修改的图书作者：")
                new_price = float(input("请输入要修改的图书价格："))
                new_stock = int(input("请输入要修改的库存数量："))
                if new_price <= 0 or new_stock < 0:
                    print("请输入要修改正确的值")
                else:
                    book["author"] = new_author
                    book["price"] = new_price
                    book["stock"] = new_stock
                    print("图书修改成功")
                    break
        else:
            print("未找到您要修改的图书")
    elif option == 3:
        name = input("请输入你要删除的图书:")
        for book in books:
            if book["name"] == name:
                del books[books.index(book)]
                print("删除成功")
                break
        else:
            print("未能找到这本书")
    elif option == 4:
        name = input("请输入你要查询的图书:")
        for book in books:
            if book["name"] == name:
                print(f"图书的名称:{book['name']},作家是:{book['author']},价格是:{book['price']}元,库存剩余:{book['stock']}本")
                break
        else:
            print("没有找到你要查询的图书")
    elif option == 5:
        if len(books)==0:
            print("图书馆内无图书信息")
        else:
            for book in books:
                print(f"图书的名称:{book['name']},作家是:{book['author']},价格是:{book['price']}元,库存剩余:{book['stock']}本")
    elif option == 6:
        if len(books)==0:
            print("图书馆内没有图书")
        else:
            total_book = len(books)
            total_stock = 0
            total_price = 0

            max_book = books[0]
            min_book = books[0]

            for book in books:
                total_stock += book["stock"]
                total_price += book["price"] * book["stock"]

                if book["price"] > max_book["price"]:
                    max_book = book
                if book["price"] < min_book["price"]:
                    min_book = book
                print("===== 图书统计 =====")
                print(f"图书的总类:{total_book}")
                print(f"库存总量为:{total_stock}本")
                print(f"总价值:{total_price}元")
                print(f"价值最高的书是{max_book['name']},价格是{max_book['price']}")
                print(f"价值最低的书是{min_book['name']},价格是{min_book['price']}")

    elif option == 7:
        print("退出系统")
        break
    else:
        print("很抱歉，该系统没有这项操作")