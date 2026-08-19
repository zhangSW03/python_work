#图书管理系统
class Book:
    def __init__(self,title,author,price,stock):
        self.title = title
        self.author = author
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"书名:{self.title} | 作者: {self.author} | 价格: {self.price} | 库存:{self.stock}"

    def update_info(self,new_author,new_price,new_stock):
        self.author = new_author
        self.price = new_price
        self.stock = new_stock

class BookSystem:
    SYSTEM_NAME = "图书管理系统"
    SYSTEM_VERSION = "1.0.0"

    def __init__(self):
        self.book_list = []

    def add_book(self):
        book_name = input("请输入你要添加的书籍名称:")
        for book in self.book_list:
            if book.title == book_name:
                print("你要添加的书已存在，请不要重复添加")
                return

        book_author = input("请输入书籍的作者:")
        book_price = float(input("请输入书籍的价格:"))
        book_stock = int(input("请输入书籍的库存数量:"))
        if book_price > 0 and book_stock >= 0:
            book = Book(book_name,book_author,book_price,book_stock)
            self.book_list.append(book)
            print("图书添加成功!")
        else:
            print("输入的价格以及库存数量不符合要求，请重新输入")

    def update_book(self):
        book_name = input("请输入你要更新的书籍名称:")
        for book in self.book_list:
            if book.title == book_name:
                book_author = input("请输入书籍的作者:")
                book_price = float(input("请输入书籍的价格:"))
                book_stock = int(input("请输入书籍的库存剩余:"))
                if book_price > 0 and book_stock >= 0:
                    book.update_info(book_author,book_price,book_stock)
                    print("书籍信息更新完成!")
                    return
                else:
                    print("输入的价格和库存数量不符合要求")
                    return
        print("未找到该图书!")

    def delete_book(self):
        book_name = input("请输入你要删除的书籍名称:")
        for book in self.book_list:
            if book.title == book_name:
                self.book_list.remove(book)
                print("删除数据成功!")
                return
        print("未找到该图书!")

    def query_book(self):
        book_name = input("请输入你要查询的书籍名称:")
        for book in self.book_list:
            if book.title == book_name:
                print(book)
                return
        print("未找到该图书!")

    def list_book(self):
        if len(self.book_list) == 0:
            print("系统内无图书")
            return
        for book in self.book_list:
            print(book)

    def run(self):
        print(f"# # # # # # {self.SYSTEM_NAME} # # # # # #")

        while True:
            print("1. 添加图书   2. 修改图书   3. 删除图书  4. 查询指定图书  5. 查询所有图书  6. 退出系统")
            choice = input("请输入你要进行的操作(1~6):")
            match choice:
                case "1" :
                    self.add_book()
                case "2" :
                    self.update_book()
                case "3" :
                    self.delete_book()
                case "4" :
                    self.query_book()
                case "5" :
                    self.list_book()
                case "6" :
                    print("退出系统")
                    break
                case _ :
                    print("系统内没有该操作")

if __name__ == "__main__":
    stu_info = BookSystem()
    stu_info.run()