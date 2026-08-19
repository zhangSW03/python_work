#通讯录管理系统
"""
>> 通讯录管理系统

1.需求说明：开发一个简单的通讯录管理系统，使用 TXT 文件存储联系人信息

2.数据存储格式（contacts.txt）：
张三|13800138001|zhangsan@example.com
李四|13800138002|lisi@example.com
王五|13800138003|wangwu@example.com

3.功能要求：
    添加联系人：输入姓名、电话、邮箱，追加到文件末尾
    查看所有联系人：读取并格式化展示所有联系人
    搜索联系人：根据姓名搜索联系人
    使用 with 上下文管理器操作文件
"""


def add_contact():
    """添加联系人"""
    print("\n【添加联系人】")
    name = input("请输入姓名：").strip()
    phone = input("请输入手机号：").strip()
    email = input("请输入邮箱：").strip()

    if not phone.isdigit() or len(phone) != 11:
        print("请输入正确手机号")
        return

    with open("contacts.txt","a",encoding="utf-8") as f:
        f.write(name+"|"+phone+"|"+email+"\n")

    print("联系人添加成功！")


def show_all_contacts():
    """查看所有联系人"""
    print("\n【所有联系人】")
    try:
        with open("contacts.txt","r",encoding="utf-8") as f:
            lines = f.readlines()
    except:
        print("暂无联系人")
        return

    if not lines:
        print("暂无联系人")
        return

    for line in lines:
        line = line.strip()
        if not line:
            continue
        name, phone, email = line.split("|")
        print(name+"|"+phone+"|"+email)

    # 如果文件不存在或为空，提示"暂无联系人"
    pass


def search_contact():
    """搜索联系人"""
    print("\n【搜索联系人】")
    keyword = input("请输入要搜索的姓名：").strip()

    try:
        with open("contacts.txt","r",encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("查还找不到联系人")

    for line in lines:
        line = line.strip()
        if not line:
            continue
        name, phone, email = line.split("|")
        if keyword == name:
            print(name+"|"+phone+"|"+email)
            return
    else:
        print("查找不到你要找的人")
    pass


def run():
    while True:
        print("\n===== 通讯录管理系统 =====")
        print("1. 添加联系人")
        print("2. 查看所有联系人")
        print("3. 搜索联系人")
        print("4. 退出")

        choice = input("请选择操作(1-4): ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            show_all_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            print("再见！")
            break
        else:
            print("无效选项！")


if __name__ == "__main__":
    run()